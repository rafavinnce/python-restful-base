from django.test import TestCase
from django.urls import reverse


class NavigationTest(TestCase):

    def test_navigation(self):
        url = reverse('test_navigation')
        response = self.client.get(url)
        assert response.status_code == 200

        # Check structure
        result = response.json()
        assert result == {'status': 'ok'}
