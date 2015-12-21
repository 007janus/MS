from django.conf.urls import patterns, include, url
from django.contrib import admin
import xadmin

xadmin.autodiscover()

#from xadmin.plugins import xversion 
#xversion.registe_models() 

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'ddMS.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),

#    url(r'^xadmin/', include(xadmin.site.urls)),
	url(r'^hostinfo$','hostinfo.views.index'),
	url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
)
