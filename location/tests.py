from django.test import TestCase
from django.urls import reverse


class LocationTest(TestCase):

    def test_location(self):
        url = reverse('test_location')
        response = self.client.get(url)
        assert response.status_code == 200

        # Check structure
        result = response.json()
        assert result == {'status': 'ok'}
