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

                 # to insert new data   
                 reg = User(name=name,email=email,password=password)
                 reg.save()

                 #to update
                 #  reg = User(id=1 , name=name,email=email,password=password)
                 #  reg.save()


                 # to delete
               #   reg = User(id=1)
               #   reg.delete()
                  

                 
       else:
            print("Comming from Get request ")
            fm = StudentRegistration()
    
       return render(request,'enroll/registeruser.html',{'form' : fm}) 
       

