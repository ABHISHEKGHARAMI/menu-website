from django.db import models
from django.conf import settings

# Create your models here.

# here we go for the model recipe which will be one to many relationship with its ingredients
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description  = models.TextField(blank=True,null=True)
    directions = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
# model for the recipe ingredient for the recipe 
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    