from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NavigationListView.as_view(), name='navigation'),
    url(r'^merchant_view/', views.NavigationListView.as_view(), name='merchant'),
    url(r'^app_open/', views.NavigationListView.as_view(), name='app'),
]