from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save

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
    
    
    # save the slug method
    def save(self,*args,**kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
 
 
# function for the article 
def slugify_instance_title(instance,save=False):
    slug = slugify(instance.title)   
    instance.slug = slug
    if save:
        instance.save()
    
    return instance
        
        
# callback function for the signal
def article_pre_save(sender,instance,*args,**kwargs):
    if instance.slug is None:
        instance.slug = slugify_instance_title(instance,save=False)
        
        
        
# connecting the article to sender
pre_save.connect(article_pre_save,sender=Article)

# call back function for post save
def article_post_save(sender,instance,created,*args,**kwargs):
    if created:
        # instance.slug = 'default slug!!!'
        slugify_instance_title(instance,save=True)
        instance.save()

post_save.connect(article_post_save,sender=Article)
    
