from django.conf.urls import url

from . import views

app_name='navigation'
urlpatterns = [
    url(r'^merchant_view', views.merchant_view, name='merchant_view')
]