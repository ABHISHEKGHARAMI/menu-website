from django.shortcuts import render
from .models import Article

# Create your views here.

# first view for the list of all article
def list_article(request):
    articles = Article.objects.all()
    return render(
        request,
        'list.html',
        {
            'articles' : articles
        }
    )
    
    
#  view for the detail view for the user
def detail_view(request,pk):
    article = Article.objects.get(id=pk)
    return render(
        request,
        'detail.html',
        {
            'article':article
        }
    )
