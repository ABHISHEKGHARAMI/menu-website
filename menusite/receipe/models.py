from django.db import models
from django.conf import settings
# Create your models here.

# receipi website for the model
class UserReceipi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    # like grilled chicken pasta
    description = models.TextField(null=True,blank=True)
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
# ingredients for receipi 
class UserReceipiIngredient(models.Model):
    receipi = models.ForeignKey(UserReceipi,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True,blank=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    direction = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
