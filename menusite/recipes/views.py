from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Create your views here.

# creating the crud operation for the recipe

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list' : qs
    }
    return render(request,
                  'recipes/list.html',
                  context=context)

@login_required
def recipe_detail_view(request,id=None):
    # qs = Recipe.objects.filter(id=id).first()
    object = get_object_or_404(Recipe,id=id,user=request.user)
    context = {
        'object' : object
    }
    return render(
        request,
        'recipes/detail.html',
        context=context
    )

# recipe create view
@login_required
def recipe_create_view(request):
    pass


# update view
@login_required
def recipe_update_view(request):
    pass
