from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse , Http404
from django.urls import reverse
from .forms import RecipeForm , RecipeIngredientForm
from .models import Recipe , RecipeIngredient

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
    # object = get_object_or_404(Recipe,id=id,user=request.user)
    hx_url = reverse("recipes:hx-detail",kwargs={'id':id})
    context = {
        'hx_url': hx_url
    }
    return render(
        request,
        'recipes/detail.html',
        context=context
    )
    
    
# for the detail view for the html view
@login_required
def recipe_detail_hx_view(request,id=None):
    # qs = Recipe.objects.filter(id=id).first()
    if not request.htmx:
        raise Http404
    try:
        object = Recipe.objects.get(id=id,user=request.user)
    except:
        object = None
        
    # if it is returning nothing
    if object is None:
        return HttpResponse('Not found')
    context = {
        'object' : object
    }
    return render(
        request,
        'recipes/partials/detail.html',
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
    # form_2 = RecipeIngredientForm(request.POST or None)
    # FormSet = modelformset_factory()
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient,form=RecipeIngredientForm,extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormSet(request.POST or None, queryset=qs)
    context = {
        'form' : form,
        'formset' : formset,
        'obj'  : obj
    }
    # check form is valid or not
    if all([form.is_valid(),formset.is_valid()]):
        # if true then save in an object
        # this is two different form but they are connected through a foreign key
        # so have to save this way
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'data saved...'
    
    # checking the valid htmx
    
    if request.htmx:
        return render(request,"recipes/partials/forms.html",context)
        
    return render(
        request,
        'recipes/create-update.html',
        context=context
    )
    
