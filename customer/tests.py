from django.test import TestCase
from django.urls import reverse


class CustomerTest(TestCase):

    def test_customer(self):
        url = reverse('customer')
        response = self.client.get(url)
        assert response.status_code == 200

        # Check structure
        result = response.json()
        assert result == {'status': 'ok'}
