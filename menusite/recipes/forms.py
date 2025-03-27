# creating the new recipe form for the user
from django import forms
from .models import Recipe , RecipeIngredient


# creating the form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','description','directions']
        
        
# creating the form for the ingredients
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name','quantity','unit']