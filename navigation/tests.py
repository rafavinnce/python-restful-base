from django.test import TestCase
from django.urls import reverse
from navigation.models import Navigation


class NavigationTest(TestCase):

    def setUp(self):
        self.navigation = Navigation.objects.create(text='Test navigation')
        Navigation.objects.create(text='Another navigation')

    def test_navigation(self):
        url = reverse('navigation')
        response = self.client.get(url)
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 2
