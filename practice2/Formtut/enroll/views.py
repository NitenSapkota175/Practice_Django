from django.shortcuts import render
from . models import Student
from . forms import StudentRegistration
from django.http import HttpResponseRedirect




def student_details(request):
    stu = Student.objects.all()
    return render(request,'enroll/studetails.html',{'stu' : stu})


def showformdata(request):

       if request.method == 'POST':
            fm = fm = StudentRegistration(request.POST)
            if fm.is_valid():
                 name = fm.cleaned_data['name']
                 email = fm.cleaned_data['email']
                 print('Name : ',name)
                 print('Email : ' ,email)

                 return HttpResponseRedirect("/success/")
       else:
            print("Comming from Get request ")
            fm = StudentRegistration()
    
            return render(request,'enroll/registeruser.html',{'form' : fm}) 
       

def success(request):
     return render(request,'enroll/success.html')