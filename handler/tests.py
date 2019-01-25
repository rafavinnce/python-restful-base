from django.test import TestCase
from django.urls import reverse
from handler.models import Handler


class HandlerTest(TestCase):

    def setUp(self):
        self.handler = Handler.objects.create(text='Test handler')
        Handler.objects.create(text='Another handler')

    def test_handler(self):
        url = reverse('handler')
        response = self.client.get(url)
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 2