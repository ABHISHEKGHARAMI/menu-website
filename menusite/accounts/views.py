from django.shortcuts import render

# Create your views here.


#  user login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        return  render(request,
                       'accounts/login.html',
                       {})
