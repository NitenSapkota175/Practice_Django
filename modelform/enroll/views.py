from django.shortcuts import render,redirect
from . models import User
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
from django.http import Http404

def home(request):
     return render(request,'enroll/home.html')

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
       

def student_details(request):
      users = User.objects.all()
      return render(request,'enroll/studetails.html' , {'stu' : users})


def updatestudent(request,pk):
      try:
        user = User.objects.get(id=pk)
      except User.DoesNotExist:
          raise Http404("User does not exist")
     
      if request.method == 'POST':
          form = StudentRegistration(request.POST, instance=user)
          if form.is_valid():
               form.save()  
               return redirect('Home')
      else:
    
        form = StudentRegistration(instance=user)
    
      return render(request, 'enroll/editstudent.html', {'form': form})