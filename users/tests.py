from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create(
            username="testuser",
            email="testuser@company.com",
            password="test123"
        )

    
    def test_usercreation(self):
        user=get_user_model().objects.get(id=1)

        self.assertEqual(user.is_staff,False)
        self.assertEqual(self.user.username,user.username)