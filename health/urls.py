from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.health, name='health'),
    url(r'^logger-service/$', views.health, name='health'),
]
