from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm,EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
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
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile update')
                fm.save()
            
        else:

            fm = EditUserProfileForm(instance=request.user)

        return render(request,'enroll/profile.html',{'name' : request.user,'forms' : fm})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_change_pass(request):


    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(user=request.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
            
        return render(request,'enroll/changepass1.html',{'forms' : fm})
    

    else:
        return HttpResponseRedirect('/login/')
    


###############   without new password    #######################
def user_change_pass1(request):


    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(user=request.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
            
        return render(request,'enroll/changepass.html',{'forms' : fm})
    

    else:
        return HttpResponseRedirect('/login/')
    

