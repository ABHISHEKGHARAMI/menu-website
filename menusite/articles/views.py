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
    
    
#  views for the search bar for the user
def article_search_view(request):
    article_object = None
    context = {}
    if request.GET:
        query = request.GET.get('q')
        article_object = Article.objects.filter(id=query)
        if article_object is not None:
            context = {
                'object': article_object
            }
    
    return render(
        request,
        'search.html',
        context=context
    )
    


# views for the creating the article
def article_create(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content is  not None:
            article_obj = Article.objects.create(title=title,content=content)
            context['object'] = article_obj
            context['created'] = True
    
    return render(request,
                  'create.html',
                  context)
