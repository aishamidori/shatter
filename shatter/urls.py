from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
   url(r'^$', views.landing),
   url(r'^company/(?P<company>\w{1,50})/$', views.company)
)
