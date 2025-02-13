from django import forms


#  creating the form for creating the user to write the article
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    
    # clean the data for the form
    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title').lower()
        print(title)
        return title