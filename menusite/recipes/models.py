from django.db import models
import pint
from django.conf import settings
from django.urls import reverse
from .validators import validate_unit_of_measurement
from .utils import number_str_to_float


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
    
    # absolute url
    def get_absolute_url(self):
        return reverse('recipes:detail',kwargs={"id" : self.id})
    
# model for the recipe ingredient for the recipe 
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True,null=True)
    unit = models.CharField(max_length=50,validators=[validate_unit_of_measurement])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    
    # here we create utility conversion for unit using the pint
    def convert_to_system(self,system='mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurements = self.quantity_as_float * ureg[self.unit]
        return measurements
    
    def  as_mks(self):
        # same as mks
        measurements = self.convert_to_system(system='mks')
        return measurements.to_base_units()
    
    def as_imperial(self):
        # for imperial system
        measurements = self.convert_to_system(system='imperial')
        return measurements.to_base_units()
    
    def to_ounces(self):
        m = self.convert_to_system()
        return m.to('ounces')
    
    
    # over-riding the save method for the float quantity
    def save(self,*args,**kwargs):
        qty = self.quantity
        qty_as_float , qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        super().save(*args,**kwargs)
    
    