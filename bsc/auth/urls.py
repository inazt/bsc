from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', {'template_name': 'auth/login.html'}),
    url(r'^accounts/logout/$', 'logout', {'template_name': 'auth/logout.html'}),
)
