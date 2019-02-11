from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^merchant_view', views.merchant_view, name='merchant_view'),
    url(r'^logger-service/merchant_view', views.merchant_view, name='merchant_view')
]