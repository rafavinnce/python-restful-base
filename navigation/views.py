from django.shortcuts import render
from navigation.models import Navigation
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import serializers


# Create your views here.
class NavigationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Navigation
        fields = ('user_id', 'created_at')


class NavigationView(RetrieveAPIView):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer


class NavigationListView(ListCreateAPIView):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
