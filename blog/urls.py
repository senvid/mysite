from django.conf.urls import patterns, url, include

from blog.views import *

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^entry/(\d+-\d+)/$', entry, name='entry'),
    url(r'^aside/$', aside),
    url(r'^archive/$', archive),
    url(r'^about/$', about),
    url(r'^test/$', test),
    
)
