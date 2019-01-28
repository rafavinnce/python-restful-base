from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.customer, name='customer'),
    url(r'^update_location/', views.customer, name='customer'),
]