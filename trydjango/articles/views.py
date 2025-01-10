from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    article_obj = Article.objects.all()
    return render(request,'articles/home.html',{
        'article':article_obj
    })
    

# list view for the article objects
def list_view(request,id):
    article_obj = Article.objects.get(id=id)
    return render(request,
                  'articles/detail.html',
                  {
                    'article':article_obj
                      }
                  )

