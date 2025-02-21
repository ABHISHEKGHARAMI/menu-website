from django.db import models
from django.conf import settings
from .validator import validate_unit_measure
# Create your models here.

# receipi website for the model
class Receipi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    # like grilled chicken pasta
    description = models.TextField(null=True,blank=True)
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
# ingredients for receipi 
class ReceipiIngredient(models.Model):
    receipi = models.ForeignKey(Receipi,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True,blank=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True,null=True)
    unit = models.CharField(max_length=50,validators=[validate_unit_measure])
    direction = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
