from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('planetarium.views',
    url(r'^blogs/(?P<blog_slug>.+)/posts/(?P<post_id>\d+)/$', 'post_display', name='post-display'),
)
