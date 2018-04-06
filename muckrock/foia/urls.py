"""
URL mappings for the FOIA application
"""

# Django
from django.conf.urls import url
from django.views.generic.base import RedirectView

# MuckRock
from muckrock.foia import views
from muckrock.foia.feeds import (
    FOIAFeed,
    LatestDoneRequests,
    LatestSubmittedRequests,
    UserDoneFeed,
    UserSubmittedFeed,
    UserUpdateFeed,
)
from muckrock.views import jurisdiction

foia_url = r'(?P<jurisdiction>[\w\d_-]+)-(?P<jidx>\d+)/(?P<slug>[\w\d_-]+)-(?P<idx>\d+)'
old_foia_url = r'(?P<jurisdiction>[\w\d_-]+)/(?P<slug>[\w\d_-]+)/(?P<idx>\d+)'

urlpatterns = [
    url(r'^$', views.RequestExploreView.as_view(), name='foia-root'),

    # List Views
    url(r'^list/$', views.RequestList.as_view(), name='foia-list'),
    url(r'^mylist/$', views.MyRequestList.as_view(), name='foia-mylist'),
    url(
        r'^organization-list/$',
        views.MyOrgRequestList.as_view(),
        name='foia-org-list',
    ),
    url(
        r'^agency-list/$',
        views.AgencyRequestList.as_view(),
        name='foia-agency-list',
    ),
    url(
        r'^list/following/$',
        views.FollowingRequestList.as_view(),
        name='foia-list-following',
    ),
    url(
        r'^list/processing/$',
        views.ProcessingRequestList.as_view(),
        name='foia-list-processing',
    ),
    # XXX new list views
    # - List of all (composer) drafts
    # - List of all composers that have multiple requests?

    # Create and Draft Views
    url(r'^create/$', views.CreateComposer.as_view(), name='foia-create'),
    url(
        r'^composer-draft/(?P<idx>\d+)/$',
        views.UpdateComposer.as_view(),
        name='foia-draft'
    ),
    url(
        r'^composer-autosave/(?P<idx>\d+)/$',
        views.autosave,
        name='foia-autosave',
    ),

    # Detail View
    url(
        r'^%s/$' % foia_url,
        views.Detail.as_view(template_name='foia/detail.html'),
        name='foia-detail',
    ),
    url(
        r'^composer/(?P<slug>[\w\d_-]+)-(?P<idx>\d+)/$',
        views.ComposerDetail.as_view(),
        name='foia-composer-detail',
    ),
    # XXX are the action views necessary?
    url(
        r'^%s/crowdfund/$' % foia_url,
        views.crowdfund_request,
        name='foia-crowdfund',
    ),
    url(
        r'^%s/files/$' % foia_url,
        views.FOIAFileListView.as_view(),
        name='foia-files',
    ),
    url(r'^%s/follow/$' % foia_url, views.follow, name='foia-follow'),
    url(r'^%s/embargo/$' % foia_url, views.embargo, name='foia-embargo'),
    url(r'^%s/pay/$' % foia_url, views.pay_request, name='foia-pay'),
    url(
        r'^%s/toggle-followups/$' % foia_url,
        views.toggle_autofollowups,
        name='foia-toggle-followups',
    ),
    # XXX redirect to composer
    url(
        r'^multi/(?P<slug>[\w\d_-]+)-(?P<pk>\d+)/$',
        views.MultiDetail.as_view(),
        name='foia-multi-detail',
    ),

    # Misc Views
    url(r'^acronyms/$', views.acronyms, name='foia-acronyms'),
    url(r'^raw_email/(?P<idx>\d+)/$', views.raw, name='foia-raw'),

    # Feeds
    url(
        r'^feeds/submitted/$',
        LatestSubmittedRequests(),
        name='foia-submitted-feed',
    ),
    url(r'^feeds/completed/$', LatestDoneRequests(), name='foia-done-feed'),
    url(r'^feeds/(?P<idx>\d+)/$', FOIAFeed(), name='foia-feed'),
    url(
        r'^feeds/submitted/(?P<username>[\w\d_.@ ]+)/$',
        UserSubmittedFeed(),
        name='foia-user-submitted-feed'
    ),
    url(
        r'^feeds/completed/(?P<username>[\w\d_.@ ]+)/$',
        UserDoneFeed(),
        name='foia-user-done-feed',
    ),
    url(
        r'^feeds/(?P<username>[\w\d_.@ ]+)/$',
        UserUpdateFeed(),
        name='foia-user-feed',
    ),

    # Files
    url(
        r'^file/(?P<pk>\d+)/embed/$',
        views.FileEmbedView.as_view(),
        name='file-embed',
    ),

    # Old URLS
    url(r'^multi/$', RedirectView.as_view(url='/foi/create/')),
    url(
        r'^create_multi/$',
        RedirectView.as_view(url='/foia/create/'),
        name='foia-create-multi',
    ),
    url(
        r'^mylist/multirequest/$',
        RedirectView.as_view(url='/foi/mylist/'),
        name='foia-mymulti',
    ),
    url(
        r'^(?P<jurisdiction>[\w\d_-]+)-(?P<idx>\d+)/$',
        jurisdiction,
        name='foia-jurisdiction',
    ),
    url(
        r'^list/user/(?P<user_name>[\w\d_.@ ]+)/$',
        RedirectView.as_view(url='/foi/list/user-%(user_name)s'),
    ),
    url(
        r'^list/tag/(?P<tag_slug>[\w\d_.@-]+)/$',
        RedirectView.as_view(url='/foi/list/tag-%(tag_slug)s')
    ),
    url(r'^(?P<action>[\w_-]+)/%s/$' % old_foia_url, views.redirect_old),
    url(
        r'^list/user-(?P<user_pk>[\w\d_.@ -]+)/$',
        RedirectView.as_view(url='/foi/list/?user=%(user_pk)s'),
        name='foia-list-user',
    ),
    url(
        r'^list/agency-(?P<agency>[\w\d_.@ -]+)-(?P<idx>\d+)/$',
        RedirectView.as_view(url='/foi/list/?agency=%(idx)s'),
        name='foia-list-agency',
    ),
    url(
        r'^list/place-(?P<jurisdiction>[\w\d_.@ -]+)-(?P<idx>\d+)/$',
        RedirectView.as_view(url='/foi/list/?jurisdiction=%(idx)s'),
        name='foia-list-jurisdiction',
    ),
    url(
        r'^list/tag-(?P<tag_slug>[\w\d_.@-]+)/$',
        RedirectView.as_view(url='/foi/list/?tags=%(tag_slug)s'),
        name='foia-list-tag',
    ),
    url(
        r'^list/status-(?P<status>[\w\d_.@ -]+)/$',
        RedirectView.as_view(url='/foi/list/?status=%(status)s'),
        name='foia-list-status',
    ),
    url(
        r'^mylist/(?P<view>\w+)/$',
        RedirectView.as_view(url='foi/mylist/'),
        name='foia-mylist-old',
    ),
]
