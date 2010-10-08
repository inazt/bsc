from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('microblog.views',
    url(r'^microblogs/(?P<microblog>.+)/tweets/new/$', 'tweet_new', name='tweet_new'),
    url(r'^microblogs/(?P<microblog>.+)/tweets/(?P<tweet_id>\d+)/delete/$', 'tweet_delete', name='tweet_delete'),
)
