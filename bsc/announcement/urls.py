from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('announcement.views',
    url(r'^news/$', 'news_list', name='news-list'),
    url(r'^news/(?P<nid>\d+)/$', 'news_display', name='news-display'),

    url(r'^event/$', 'event_list', name='event-list'),
    url(r'^event/(?P<nid>\d+)/$', 'event_display', name='event-display'),
)
