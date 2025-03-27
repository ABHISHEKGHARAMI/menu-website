# creating the new recipe form for the user
from django import forms
from .models import Recipe , RecipeIngredient


# creating the form
class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-css'
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder" : "recipe name"
    }))
    class Meta:
        model = Recipe
        fields = ['name','description','directions']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields['name'].widget.attrs.update({'class':'form-control-2'})
        
        for field in self.fields:
            new_data = {
                'placeholder': f'Recipe {str(field)}',
                'class': 'form-controll'
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        
        
# creating the form for the ingredients
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name','quantity','unit']