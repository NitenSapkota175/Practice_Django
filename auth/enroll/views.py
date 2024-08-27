from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profile/')
                
        else:
            fm = SignUpForm()
        return render(request,'enroll/signup.html',{'forms' : fm})
    else:
          return HttpResponseRedirect('/profile/')


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            fm = AuthenticationForm(request=request ,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upass = fm.cleaned_data.get('password')
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"You are logged in!")
                    return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()   
        return render(request,'enroll/userlogin.html',{'forms' : fm})
    
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):

    if request.user.is_authenticated:

        return render(request,'enroll/profile.html',{'name' : request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')