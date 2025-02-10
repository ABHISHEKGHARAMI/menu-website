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
