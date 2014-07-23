from django.conf.urls import patterns, url
from KPSApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='KPS-index'),
    url(r'^about/$', views.about, name='KPS-about'),
    url(r'^check/$', views.check, name='KPS-check'),
)