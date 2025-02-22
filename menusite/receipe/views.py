from django.shortcuts import render
from .models import Receipi
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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
def receipi_create_view(request,id=None):
    form = ReceipiForm(request.POST or None)
    return
# receipi update view
@login_required
def receipi_update_view(request,id):
    form = ReceipiForm(request.POST or None)
    obj = get_object_or_404(Receipi,id=id,user=request.user)
