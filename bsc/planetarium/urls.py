from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('planetarium.views',
    url(r'^blogs/(?P<blog_slug>.+)/posts/(?P<post_id>\d+)/$', 'post_display', name='post-display'),
    url(r'^blogs/(?P<blog_slug>.+)/posts/(?P<post_id>\d+)/edit/$', 'post_edit_form', name='post-edit-form'),
    url(r'^blogs/(?P<blog_slug>.+)/posts/new/$', 'post_new_form', name='post-new-form'),
)
