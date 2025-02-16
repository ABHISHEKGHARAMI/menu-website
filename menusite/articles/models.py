from django.db import models

# Create your models here.

# article model
class Article(models.Model):
    # two field right now
    title = models.CharField(max_length=250)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
