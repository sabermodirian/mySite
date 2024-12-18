from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username , password=password)
                if user is not None:
                    print(user)
                    login(request , user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form':form}          
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required     # if request.user.is_authenticated:
def logout_view(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                return redirect(reverse('accounts:login'))    
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')