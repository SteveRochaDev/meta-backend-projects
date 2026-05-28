from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MenuItem

class MenuItemTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = MenuItem.objects.create(
            name="Test Pizza",
            price=12.99,
            menu_description="Delicious pizza"
        )

    def test_get_menu_items(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_menu_item(self):
        data = {
            "name": "Grilled Salmon",
            "price": 18.99,
            "menu_description": "Fresh salmon with herbs"
        }
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)