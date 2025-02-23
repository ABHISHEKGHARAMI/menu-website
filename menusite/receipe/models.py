from django.db import models
from django.conf import settings
from .validator import validate_unit_measure
from .utils import number_str_to_float
import pint
from django.urls import reverse
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
    
    
    def get_absolute_url(self):
        return reverse('receipe:detail',kwargs={'id':self.id})
    
    
    
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
    
    def get_absolute_url(self):
        return self.receipi.get_absolute_url()

    
    # solving the unit problem
    def convert_to_system(self,system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system = system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement
    
    
    # as ounces
    def to_ounces(self):
        m = self.convert_to_system()
        return m.to('ounces')
    
    # as meter , kilo and second
    def as_mks(self):
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()
    
    # as imperial mile , pound , second
    def as_imperial(self):
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()
    
    
    # overriding the save method for the changing the quantity to str to float
    def save(self,*args,**kwargs):
        qty = self.quantity
        quantity_as_float, quantity_as_float_stat = number_str_to_float(qty)
        if quantity_as_float_stat == True:
            self.quantity_as_float = quantity_as_float
        else:
            self.quantity_as_float = None
        super().save(*args,**kwargs)
    
