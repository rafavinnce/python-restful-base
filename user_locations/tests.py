from django.test import TestCase
from django.urls import reverse


class UserLocationsTest(TestCase):

    def test_user_locations(self):
        url = reverse('test_user_locations')
        response = self.client.get(url)
        assert response.status_code == 200

        # Check structure
        result = response.json()
        assert result == {'status': 'ok'}
