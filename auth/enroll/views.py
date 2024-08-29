from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm,EditUserProfileForm,EditAdimProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
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

            if request.user.is_superuser == True:
                fm = EditAdimProfileForm(request.POST,instance=request.user)
                user = User.objects.all()

            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
                user = None
            if fm.is_valid():
                messages.success(request,'Profile updated')
                fm.save()
            
        else:
            if  request.user.is_superuser == True:
                fm = EditAdimProfileForm(instance=request.user)
                user = User.objects.all()
            else: 
                fm = EditUserProfileForm(instance=request.user)
                user = None
        return render(request,'enroll/profile.html',{'name' : request.user,'forms' : fm , 'users' : user})
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
    

def show_user_details(request,pk):
    if request.user.is_authenticated:
        pi = User.objects.get(id=pk)
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request , f"You have the user details {pi}")
                return HttpResponseRedirect('/profile/')
        else:
             fm = EditUserProfileForm(instance=pi)

    return render(request,'enroll/userdetails.html' , {'forms' : fm}) 