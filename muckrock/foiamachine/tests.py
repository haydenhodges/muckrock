"""
Tests for the FOIAMachine application.
"""

from django.contrib import auth
from django.template.loader import render_to_string
from django.test import TestCase


from django_hosts.resolvers import reverse
from nose.tools import eq_, ok_

from muckrock.factories import UserFactory, AgencyFactory
from muckrock.foiamachine import factories, forms, models, views
from muckrock.jurisdiction.factories import StateJurisdictionFactory
from muckrock.test_utils import http_get_response, http_post_response


class TestHomepage(TestCase):
    """The homepage should provide information about FOIAMachine and helpful links."""
    def setUp(self):
        self.view = views.Homepage.as_view()
        self.url = reverse('index', host='foiamachine')

    def test_unauthenticated(self):
        """The homepage should return 200."""
        response = http_get_response(self.url, self.view)
        eq_(response.status_code, 200)

    def test_authenticated(self):
        """If the user is authenticated, the homepage should redirect to their profile."""
        user = UserFactory()
        response = http_get_response(self.url, self.view, user)
        eq_(response.status_code, 302)
        eq_(response.url, reverse('profile', host='foiamachine'))


class TestLogin(TestCase):
    """Users should be able to log in."""
    def setUp(self):
        self.view = auth.views.login
        self.url = reverse('login', host='foiamachine')

    def test_ok(self):
        """Login should return 200."""
        response = http_get_response(self.url, self.view)
        eq_(response.status_code, 200)


class TestSignup(TestCase):
    """Users should be able to sign up."""
    def setUp(self):
        self.view = views.Signup.as_view()
        self.url = reverse('signup', host='foiamachine')

    def test_ok(self):
        """Signup should return 200."""
        response = http_get_response(self.url, self.view)
        eq_(response.status_code, 200)

    def test_signup(self):
        """Posting the required information to sign up should create an account,
        log the user into the account, create a profile for their account,
        and return a redirect to the profile page."""
        data = {
            'username': 'TestUser',
            'email': 'test@email.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'test',
            'password2': 'test',
        }
        response = http_post_response(self.url, self.view, data)
        eq_(response.status_code, 302, 'The response should redirect.')
        eq_(response.url, reverse('profile', host='foiamachine'))
        user = auth.models.User.objects.get(username=data['username'])
        ok_(user, 'The user should be created.')
        ok_(user.profile, 'The user should be given a profile.')


class TestProfile(TestCase):
    """Users should be able to view their profile once they're logged in."""
    def setUp(self):
        self.view = views.Profile.as_view()
        self.url = reverse('profile', host='foiamachine')

    def test_unauthenticated(self):
        """Authentication should be required to view the profile page."""
        response = http_get_response(self.url, self.view)
        eq_(response.status_code, 302, 'The view should redirect.')
        eq_(response.url, reverse('login', host='foiamachine') + '?next=' + self.url,
            'The redirect should point to the login view, with this as the next view.')

    def test_authenticated(self):
        """When authenticated, the view should return 200."""
        user = UserFactory()
        response = http_get_response(self.url, self.view, user)
        eq_(response.status_code, 200)


class TestFoiaMachineRequestCreateView(TestCase):
    """Users should be able to create a new request, as long as they are logged in."""
    def setUp(self):
        self.view = views.FoiaMachineRequestCreateView.as_view()
        self.url = reverse('foi-create', host='foiamachine')
        self.user = UserFactory()

    def test_unauthenticated(self):
        """Unauthenticated users should be redirected to the login screen."""
        response = http_get_response(self.url, self.view)
        eq_(response.status_code, 302, 'The view should redirect.')
        eq_(response.url, reverse('login', host='foiamachine') + '?next=' + self.url,
            'The redirect should point to the login view, with this as the next view.')

    def test_authenticated(self):
        """When authenticated, the view should return 200."""
        user = UserFactory()
        response = http_get_response(self.url, self.view, user)
        eq_(response.status_code, 200)

    def test_create(self):
        """Posting a valid creation form should create a request and redirect to it."""
        title = 'Test Request'
        request_language = 'Lorem ipsum'
        jurisdiction = StateJurisdictionFactory().id
        form = forms.FoiaMachineRequestForm({
            'title': title,
            'request_language': request_language,
            'jurisdiction': jurisdiction
        })
        ok_(form.is_valid())
        response = http_post_response(self.url, self.view, form.data, self.user)
        eq_(response.status_code, 302, 'When successful the view should redirect to the request.')
        foi = models.FoiaMachineRequest.objects.first()
        eq_(response.url, foi.get_absolute_url())


class TestFoiaMachineRequestDetailView(TestCase):
    """Anyone can see the request, as long as they have the link."""
    def setUp(self):
        self.foi = factories.FoiaMachineRequestFactory()
        self.view = views.FoiaMachineRequestDetailView.as_view()
        self.kwargs = {
            'slug': self.foi.slug,
            'pk': self.foi.pk,
        }
        self.url = reverse('foi-detail', host='foiamachine', kwargs=self.kwargs)

    def test_get(self):
        """Anyone can see the request page."""
        response = http_get_response(self.url, self.view, **self.kwargs)
        eq_(response.status_code, 200)


class TestFoiaMachineRequest(TestCase):
    """The FOIA Machine Request should store information we need to send a request."""
    def setUp(self):
        self.user = UserFactory()
        self.title = 'Test Request'
        self.request_language = 'Lorem ipsum'
        self.agency = AgencyFactory()
        self.jurisdiction = self.agency.jurisdiction
        self.foi = factories.FoiaMachineRequestFactory(
            user=self.user,
            title=self.title,
            request_language=self.request_language,
            jurisdiction=self.jurisdiction,
        )

    def test_create(self):
        """Requests should only require a user, a title,
        request language, and a jurisdiction to be created."""
        foi = models.FoiaMachineRequest.objects.create(
            user=self.user,
            title=self.title,
            request_language=self.request_language,
            jurisdiction=self.jurisdiction,
        )
        ok_(foi, 'The request should be created.')
        ok_(foi.slug, 'The slug should be created automatically.')

    def test_unicode(self):
        """Requests should use their titles when converted to unicode."""
        eq_(unicode(self.foi), self.foi.title,
            'The Unicode representation should be the title.')

    def test_get_absolute_url(self):
        """Request urls should include their slug and their id."""
        kwargs = {
            'slug': self.foi.slug,
            'pk': self.foi.pk,
        }
        actual_url = self.foi.get_absolute_url()
        expected_url = reverse('foi-detail', host='foiamachine', kwargs=kwargs)
        eq_(actual_url, expected_url)

    def test_generate_letter(self):
        """Using default information, the request should be able to generate a letter."""
        template = 'text/foia/request.txt'
        context = {
            'jurisdiction': self.foi.jurisdiction,
            'document_request': self.foi.request_language,
            'user_name': self.foi.user.get_full_name()
        }
        expected_letter = render_to_string(template, context=context)
        actual_letter = self.foi.generate_letter()
        eq_(actual_letter, expected_letter)
