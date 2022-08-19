from django.shortcuts import render,redirect
from .forms import *
from  django.contrib.auth import authenticate
from  django.contrib.auth import logout as lgo
from  django.contrib.auth import login as lg
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                lg(request,user)
                messages.success(request,'you logged in successfully','success')
                return redirect('info:home')
            else:
                messages.error(request,'username or password is wrong','alert')
    else:
        form = UserLoginForm
    return render(request,'accounts/login.html',{'form':form})


#------------------------------------------------------------------------------------------------
def logout(request):
    lgo(request)
    messages.success(request,'you logged out successfully','success')
    return redirect('info:home')
#------------------------------------------------------------------------------------------------
def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(User.objects.all().count()-1,cd['password'],cd['name'])
            # user.username =
            user.save()
            messages.success(request,'you registered successfully','success')
            return redirect('info:home')
        else:
            messages.error(request,'something is wrong','alert')
    else:
        form = UserRegistrationForm
    return render(request,'accounts/signUp.html',{'form':form})
