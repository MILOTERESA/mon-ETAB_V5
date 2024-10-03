from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from base.models.adress import AddressModel


# Create your tests here.

class TestIntegrationsAdress(APITestCase):
    
    def test_create_adress(self):
    
        url= reverse("address-list")  
        data = {
            "city"   : "Abidjan" ,
            "street" :"plateau",
            "country":"CI",
            "name"   : "Milo"
        }
            
            
    
        response =self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AddressModel.objects.count(), 1)