from django.conf.urls.defaults import patterns, include, url
from sync.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sme.views.home', name='home'),
    # url(r'^sme/', include('sme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^upload/$', handle_upload),
    (r'^delete/$', handle_delete),
    (r'^bulk_upload/$', bulk_upload),
    (r'^bulk_delete/$', bulk_delete)
)
