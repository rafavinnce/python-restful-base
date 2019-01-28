from django.test import TestCase
from django.urls import reverse
from location.models import Location


class LocationTest(TestCase):

    def setUp(self):
        self.location = Location.objects.create(text='Test location')
        Location.objects.create(text='Another location')

    def test_location(self):
        url = reverse('location')
        response = self.client.get(url)
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 2
