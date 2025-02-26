from django.shortcuts import render , redirect
from .models import Receipi, ReceipiIngredient
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ReceipiForm, ReceipiIngredientForm
from django.forms.models import modelformset_factory
# Create your views here.


# list view for the receipe 
@login_required
def receipi_list_view(request):
    qs = Receipi.objects.filter(user=request.user)
    return render(
        request,
        'receipi/list.html',
        {
            'object_list': qs
        }
    )

# detail view for the receipe
@login_required
def receipi_detail_view(request,id=None):
    qs = get_object_or_404(Receipi,id=id,user=request.user)
    return render(
        request,
        'receipi/detail.html',
        {
            'object' : qs
        }
    )

# receipe create view
@login_required
def receipi_create_view(request):
    form = ReceipiForm(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
        
    return render(
        request,
        'receipi/create-update.html',
        context=context
    )
# receipi update view
@login_required
def receipi_update_view(request,id=None):
    obj = get_object_or_404(Receipi,id=id,user=request.user)
    form = ReceipiForm(request.POST or None , instance = obj)
    # form_2 = ReceipiIngredientForm(request.POST or None)
    qs = obj.receipiingredient_set.all()
    ReceipiIngredientFormset = modelformset_factory(ReceipiIngredient,form=ReceipiIngredientForm, extra=0)
    formset = ReceipiIngredientFormset(request.POST or None , queryset=qs)
    context = {
        'form' : form,
        'formset' : formset ,
        'object': obj
    }
    
    if all([form.is_valid(),formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        # child = form_2.save(commit=False)
        # child.receipe = parent
        # child.save()
        # context['message'] = 'data updated.'
        # return redirect('receipe:list')
        for form in formset:
            child = form.save(commit=False)
            child.receipi = parent
            child.save()
        context['message'] = 'data saved'
        # return redirect("receipe:list")
    return render(
        request,
        'receipi/create-update.html',
        context
    )
        
