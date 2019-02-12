from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.location, name='location'),
    url(r'^logger-service/$', views.location, name='location'),
    url(r'^background', views.background, name='background'),
    url(r'^logger-service/background', views.background, name='background')
]