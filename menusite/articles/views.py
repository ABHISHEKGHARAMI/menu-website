from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
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
