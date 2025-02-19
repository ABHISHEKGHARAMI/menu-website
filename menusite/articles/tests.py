from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title
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
        self.number_of_article = 500
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
        
        
    # test case for the queryset slug
    def test_not_slug_qs(self):
        qs = Article.objects.exclude(slug__iexact='testing')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug,slugified_title)
            
            
    # test case for the unique slug length
    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slug = []
        for i in range(0,25):
            instance = slugify_instance_title(obj,save=False)
            new_slug.append(instance.slug)
        
        
        unique_slug = list(set(new_slug))
        self.assertEqual(len(unique_slug),len(new_slug))
        
        
    # test with the list object

    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug',flat=True)
        unique_slug = list(set(slug_list))
        self.assertEqual(len(slug_list),len(unique_slug))
        
        
    # test the search query set
    def test_search_query(self):
        qs = Article.objects.search(query='testing')
        self.assertEqual(qs.count(),self.number_of_article)
        
        qs = Article.objects.search(query='testing')
        self.assertEqual(qs.count(),self.number_of_article)
        
