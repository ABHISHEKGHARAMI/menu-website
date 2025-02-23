from django import forms
from .models import Receipi


# generate the form for the create view
class ReceipiForm(forms.ModelForm):
    class Meta:
        model = Receipi
        fields = ['name', 'description', 'directions']
