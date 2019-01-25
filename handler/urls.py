from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HandlerListView.as_view(), name='handler'),
]