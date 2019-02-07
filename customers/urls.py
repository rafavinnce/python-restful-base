from django.conf.urls import url

from . import views

app_name='customers'
urlpatterns = [
    url(r'^update_location', views.update_location, name='update_location')
]