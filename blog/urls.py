from django.conf.urls import patterns, url, include

from blog.views import *

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^archive/', archive),
    url(r'^about/$', about),
    url(r'^test/$', test),
    
)