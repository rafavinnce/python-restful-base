from django.shortcuts import render
from location.models import Location
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import serializers


# Create your views here.
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('user_id', 'created_at')


class LocationView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
