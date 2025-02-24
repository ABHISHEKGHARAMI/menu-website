from django import forms
from .models import Receipi, ReceipiIngredient


# generate the form for the create view
class ReceipiForm(forms.ModelForm):
    # error_css_class = 'error-class'
    # required_css_class = 'required-class'
    # name = forms.CharField(widget=forms.TextInput(attrs={"class":'flow-control',
    #                                                      "placeholder":'receipe name'}))
    class Meta:
        model = Receipi
        fields = ['name', 'description', 'directions']
        
    # overriding the forms
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.forms['name'].widget.attrs.update({'class':'form-control'})
        # for the fields 
        
        for field in self.fields:
            new_data = {
                'placeholder': f'enter receipe {str(field)}',
                'class': 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        # changing the description and directions for the rows
        self.fields['description'].widget.attrs.update({'rows':2})
        self.fields['directions'].widget.attrs.update({'rows': 3})
# form for the ingredient in the receipi
class ReceipiIngredientForm(forms.ModelForm):
    class Meta:
        model = ReceipiIngredient
        fields = ['name','quantity','unit']
