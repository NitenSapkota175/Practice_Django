from django.shortcuts import render
from . models import User
from . forms import StudentRegistration
from django.http import HttpResponseRedirect

def showformdata(request):

       if request.method == 'POST':
            fm = fm = StudentRegistration(request.POST)
            if fm.is_valid():
                 name = fm.cleaned_data.get('name')
                 email = fm.cleaned_data.get('email')
                 password = fm.cleaned_data.get('password')
                 rpassword = fm.cleaned_data.get('repassword')
              
                 reg = User(name=name,email=email,password=password)

                 #if you want to update the existing user you can do this you just have to give the id 
               
               # this save() method works as INSERT AND UPDATE as well , if you give a id it will work as id 
               #   reg = User(id=1, name=name,email=email,password=password)


               # to delete
               # reg = User(id=1)
               #reg.delete()

               
                 reg.save()

                 
       else:
            print("Comming from Get request ")
            fm = StudentRegistration()
    
       return render(request,'enroll/registeruser.html',{'form' : fm}) 
       

