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
                 password = fm.cleaned_data['password']
                 rpassword = fm.cleaned_data['rpassword']
               #   rollno = fm.cleaned_data['roll']
               #   agree = fm.cleaned_data['agree']
               #   price = fm.cleaned_data['price']
               #   rate = fm.cleaned_data['rate']
                 print('Name : ',name)
                 print('Email : ' ,email)
                 print('password : ' ,password)
                 print('rpassword : ' ,rpassword)

               #   print('roll : ',rollno)
               #   print('agree : ' ,agree)
               #   print('price : ',price)
               #   print('Rate : ',rate)
                #  return HttpResponseRedirect("/success/")

                 
       else:
            print("Comming from Get request ")
            fm = StudentRegistration()
    
       return render(request,'enroll/registeruser.html',{'form' : fm}) 
       

def success(request):
     return render(request,'enroll/success.html')