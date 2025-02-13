from django import forms
from django.db.models import Q
from .models import Article

#  creating the form for creating the user to write the article
# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea)
    
    
#     # clean the data for the form
#     def clean_title(self):
#         cleaned_data = self.cleaned_data
#         title = cleaned_data.get('title').lower()
#         content = cleaned_data.get('content')
#         if title is None:
#             raise forms.ValidationError('title is required for article to submit.')
#         qs = Article.objects.filter(Q(title__icontains=title) or Q(content__icontains=content))
#         if qs.exists():
#             self.add_error('title or content',f"{title} or {content} is in use please change that!!!")
#         print(title)
#         return title



# trying the article model from
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        
        
    # for cleaning  the data
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        content = data.get('content')
        qs = Article.objects.filter(Q(title__icontains=title) or Q(content__icontains=content))
        if qs.exists():
            self.add_error("title or contents",f"{title} or{content} are already taken")
        return data