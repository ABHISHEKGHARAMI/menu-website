from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import slugify_instance_title
from django.urls import reverse

# Create your models here.

# article model
class Article(models.Model):
    # two field right now
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
    
    
    # creating the absolute view for the article
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug":self.slug})
    
    
    
    # save the slug method
    def save(self,*args,**kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
 
 

        
# callback function for the signal
def article_pre_save(sender,instance,*args,**kwargs):
    if instance.slug is None:
        slugify_instance_title(instance,save=False)
        
        
        
# connecting the article to sender
pre_save.connect(article_pre_save,sender=Article)

# call back function for post save
def article_post_save(sender,instance,created,*args,**kwargs):
    if created:
        # instance.slug = 'default slug!!!'
        slugify_instance_title(instance,save=True)
        # instance.save()

post_save.connect(article_post_save,sender=Article)
    
