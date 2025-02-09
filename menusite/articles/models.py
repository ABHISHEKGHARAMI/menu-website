from django.db import models

# Create your models here.

# article model
class Article(models.Model):
    # two field right now
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    
    def __str__(self):
        return self.title
    
