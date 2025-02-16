from django.test import TestCase

from django.conf import settings
from django.contrib.auth.password_validation import validate_password
# Create your tests here.


class ArticleTest(TestCase):
    
    # test case for the secret key strength
    def test_password_strength(self):
        password = settings.SECRET_KEY
        try:
            is_strong = validate_password(password)
        except e:
            msg = f"Bad Secret key : {e}"
            self.fail(e)
         
