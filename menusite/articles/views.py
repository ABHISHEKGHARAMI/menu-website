from django.shortcuts import render , redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm 
from django.http import Http404
from django.db.models import Q
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
def detail_view(request,slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoNotExist:
            raise Http404
            
        except:
            raise Http404
    return render(
        request,
        'detail.html',
        {
            'article':article_obj
        }
    )
    
    
#  views for the search bar for the user
def article_search_view(request):
    article_object = None
    context = {}
    if request.GET:
        query = request.GET.get('q')
        if query is None:
            article_object = Article.objects.all()
        else:
            article_object = Article.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query))
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
@login_required
def article_create(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # if title and content is  not None:
            #     article_obj = Article.objects.create(title=title,content=content)
            article_obj = form.save()
            context['object'] = article_obj
            context['created'] = True
    
    return render(request,
                  'create.html',
                  context)
