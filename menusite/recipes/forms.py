# creating the new recipe form for the user
from django import forms
from .models import Recipe


# creating the form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','description','directions']