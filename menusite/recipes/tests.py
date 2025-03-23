from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


# creating the user
User = get_user_model()


# Here is the test case for the user
class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='Agh',password='Abhi1998@')
        
    # check the password
    def test_user_pw(self):
        check = self.user_a.check_password(raw_password='Abhi1998@')
        self.assertTrue(check)