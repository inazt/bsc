import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^twitter_like/', include('twitter_like.foo.urls')),
    (r'^$', 'twitter_like.microblog.views.index'),
    (r'^', include('twitter_like.microblog.urls')),
    (r'^', include('twitter_like.auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^m/(?P<path>.*)$', serve, {
            'document_root': os.path.join(os.path.dirname(__file__), 'media')
        })
    )
