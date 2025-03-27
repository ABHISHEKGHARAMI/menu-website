from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm , RecipeIngredientForm
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
    form = RecipeForm(request.POST or None)
    context = {
        'form' : form
    }
    # check form is valid or not
    if form.is_valid():
        # if true then save in an object 
        obj = form.save(commit=False)
        # saving the user
        obj.user = request.user
        # then save the data
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(
        request,
        'recipes/create-update.html',
        context=context
    )


# update view
@login_required
def recipe_update_view(request,id=None):
    obj = get_object_or_404(Recipe,id=id,user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    context = {
        'form' : form,
        "form_2" : form_2,
        'obj'  : obj
    }
    # check form is valid or not
    if all([form.is_valid(),form_2.is_valid()]):
        # if true then save in an object
        form.save(commit=False)
        form_2.save(commit=False)
        context['message'] = 'data saved...'
    return render(
        request,
        'recipes/create-update.html',
        context=context
    )
    
