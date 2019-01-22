from django.shortcuts import render
from handler.models import Handler
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import serializers


# Create your views here.
class HandlerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Handler
        fields = ('text', 'timestamp')


class HandlerView(RetrieveAPIView):
    queryset = Handler.objects.all()
    serializer_class = HandlerSerializer


class HandlerListView(ListCreateAPIView):
    queryset = Handler.objects.all()
    serializer_class = HandlerSerializer