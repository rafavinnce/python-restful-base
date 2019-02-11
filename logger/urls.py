from django.conf.urls import url, include
from rest_framework import serializers, viewsets, routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^health', include('health.urls')),
    url(r'^logger-service/health', include('health.urls')),
    url(r'^location', include('location.urls')),
    url(r'^logger-service/location', include('location.urls')),
    url(r'^location/', include('location.urls')),
    url(r'^logger-service/location/', include('location.urls')),
    url(r'^navigation/', include('navigation.urls')),
    url(r'^logger-service/navigation/', include('navigation.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^logger-service/customers/', include('customers.urls')),
]
