from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from api.resources import *

v1_api = Api(api_name='v1')
v1_api.register(FileResource())
v1_api.register(DirectoryResource())

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
  
)
