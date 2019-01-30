from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.location, name='location'),
    url(r'^update_location', views.update_location, name='update_location'),
    url(r'^background', views.background, name='background')
]