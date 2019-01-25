from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LocationListView.as_view(), name='location'),
    url(r'^background/', views.LocationListView.as_view(), name='background'),
    url(r'^background/test/', views.LocationListView.as_view(), name='background'),
    url(r'^test/', views.LocationListView.as_view(), name='test'),
]