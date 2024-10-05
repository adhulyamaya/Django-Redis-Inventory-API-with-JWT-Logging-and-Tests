from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from .models import Inventory_Items  # Adjust the import based on your project structure

class InventoryItemsTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Obtain a JWT token for the user
        self.token = AccessToken.for_user(self.user)
        # Set the authorization header for the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        # Create an inventory item for further tests
        self.item = Inventory_Items.objects.create(
            name="Test Item",
            description="Test Description",
            unit_price=10.99,
            quantity=10,
            category="Test Category",
            supplier="Test Supplier"
        )
        self.url = reverse('item-list-create')  # (/api/items/)
        self.detail_url = reverse('item-detail', args=[self.item.id])  # (/api/items/<id>/)

    def test_create_item(self):
        data = {
            "name": "New Item",
            "description": "New Item Description",
            "unit_price": 5.50,
            "quantity": 20,
            "category": "New Category",
            "supplier": "New Supplier"
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)  # To see the full response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)
        
    def test_update_item(self):
        updated_data = {
            "name": "Updated Item",
            "description": "Updated Item Description",
            "unit_price": 7.50,
            "quantity": 15,
            "category": "Updated Category",
            "supplier": "Updated Supplier"
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Item")

    # def test_delete_item(self):
    #     response = self.client.delete(self.detail_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     # Verify the item no longer exists
    #     response = self.client.get(self.detail_url)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




    
        
