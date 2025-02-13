from django import forms


#  creating the form for creating the user to write the article
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    
    
    # clean the data for the form
    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title').lower()
        if title is None:
            raise forms.ValidationError('title is required for article to submit.')
        print(title)
        return title