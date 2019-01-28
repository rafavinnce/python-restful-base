from django.test import TestCase
from django.urls import reverse


class HealthTest(TestCase):

    def test_handler(self):
        url = reverse('health')
        response = self.client.get(url)
        assert response.status_code == 200

        # Check structure
        result = response.json()
        assert result == {'status': 'ok', 'db': {'status': 'ok'}}
