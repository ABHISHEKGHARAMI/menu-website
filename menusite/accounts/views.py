from django.shortcuts import render , redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        
        if user is None:
            context = {'error' : 'Invalid authentication'}
            return render(request,'accounts/login.html',context=context)
        
        #  login the user
        login(request,user)
        return redirect('articles:list_article')
        
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
