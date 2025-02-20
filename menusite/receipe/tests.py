from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Receipi , ReceipiIngredient
# Create your tests here.


User = get_user_model()


# setting the test case for the user
class UserTest(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('test',password='abc123@')
        
    # first test case for the password check
    def test_check_pw(self):
        checked = self.user_a.check_password('abc123@')
        self.assertTrue(checked)
        
        
        
        

#  setting up for the Receipe model
class ReceipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('test',password='abc123@')
        
    # first case for the test count
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)
        
        
    #  second case for the test count for the setting receipe
    def test_receipi_count(self):
        user = self.user_a
        qs = user.receipi_set.all()
        self.assertEqual(qs.count(),0)
        
        
