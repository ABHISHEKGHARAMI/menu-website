from django.test import TestCase

from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from .models import Article
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
            
    #  setting up the test database
    def setUp(self):
        Article.objects.create(title='hello',content='testing')
            
    #  test case for the database data exist or not
    def test_queryset_exist(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
        
    # test case for the database count
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),1)
         
