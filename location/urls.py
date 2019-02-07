from django.conf.urls import url

from . import views

app_name='location'
urlpatterns = [
    url(r'^$', views.location, name='location'),
    url(r'^background', views.background, name='background')
]