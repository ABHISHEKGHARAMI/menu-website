from django.test import TestCase

from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from .models import Article
from django.utils.text import slugify
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
        self.number_of_article = 5
        for i in range(0,self.number_of_article):
            Article.objects.create(title='testing',content='testing slugify content!!')
            
    #  test case for the database data exist or not
    def test_queryset_exist(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
        
    # test case for the database count
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),self.number_of_article)
        
        
    # test case for the slug
    def test_slug_qs(self):
        obj = Article.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)
