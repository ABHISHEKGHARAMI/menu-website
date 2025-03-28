from django.shortcuts import render , redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Create your views here.



# user registration form
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('accounts:login')
    return render(
        request,
        'accounts/register.html',
        {
            'form':form
        }
    )


#  user login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('articles:list_article')
    else:
        form = AuthenticationForm(request)
        
    return  render(request,
                       'accounts/login.html',
                       {
                        
                       })
    
    
    

#  user logout view for the user
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
        
    return render(request,
                  'accounts/logout.html',{})
