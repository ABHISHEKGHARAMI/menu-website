from django.test import TestCase

from django.conf import settings
# Create your tests here.


class ArticleTest(TestCase):
    
    # test case for the secret key strength
    def test_password_strength(self):
        password = settings.SECRET_KEY
        self.assertNotEqual(password,'abc1234@')
