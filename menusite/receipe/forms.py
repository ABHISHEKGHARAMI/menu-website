from django import forms
from .models import Receipi, ReceipiIngredient


# generate the form for the create view
class ReceipiForm(forms.ModelForm):
    class Meta:
        model = Receipi
        fields = ['name', 'description', 'directions']
        
        
# form for the ingredient in the receipi
class ReceipiIngredientForm(forms.ModelForm):
    class Meta:
        model = ReceipiIngredient
        fields = ['name','quantity','unit']
