from django.shortcuts import render , redirect
from .models import Receipi
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ReceipiForm, ReceipiIngredientForm
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
    form_2 = ReceipiIngredientForm(request.POST or None)
    context = {
        'form' : form,
        'form_2' : form_2 , 
        'object': obj
    }
    
    if all([form.is_valid(),form_2.is_valid()]):
        form.save()
        context['message'] = 'data updated.'
        return redirect('receipe:list')
    return render(
        request,
        'receipi/create-update.html',
        context = context
    )
        
