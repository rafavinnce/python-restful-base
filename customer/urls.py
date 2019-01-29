from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^update_location', views.update_location, name='update_location')
]