from django.test import TestCase
from django.urls import reverse
from event.models import Event


class EventTest(TestCase):

    def setUp(self):
        self.event_merchant_view = Event.objects.create(text='Test Event')
        Event.objects.create(text='Event')

    def test_event(self):
        url = reverse('Event')
        response = self.client.get(url)
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 2
