from django.test import TestCase
from user.models.user import CustomUserModel


# Create your tests here.

class TestUnitUserModel(TestCase):

    def test_create_user(self):
        user= CustomUserModel.objects.create(username="milo" , password="1234")
        self.assertEqual(user.username, "milo")

    