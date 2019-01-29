from django.shortcuts import render
from event_merchant_view.models import EventMerchantView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import serializers


# Create your views here.
class EventMerchantViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventMerchantView
        fields = ('text', 'timestamp')


class EventMerchantViewView(RetrieveAPIView):
    queryset = EventMerchantView.objects.all()
    serializer_class = EventMerchantViewSerializer


class EventMerchantViewListView(ListCreateAPIView):
    queryset = EventMerchantView.objects.all()
    serializer_class = EventMerchantViewSerializer
