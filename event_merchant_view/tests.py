from django.test import TestCase
from django.urls import reverse
from event_merchant_view.models import EventMerchantView


class EventMerchantViewTest(TestCase):

    def setUp(self):
        self.event_merchant_view = EventMerchantView.objects.create(text='Test EventMerchantView')
        EventMerchantView.objects.create(text='EventMerchantView')

    def test_event_merchant_view(self):
        url = reverse('EventMerchantView')
        response = self.client.get(url)
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 2
