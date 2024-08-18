from django.shortcuts import render
from . models import Student
from . forms import StudentRegistration
# Create your views here.

def student_details(request):
    stu = Student.objects.all()

    # only one object by id 
    # stu = Student.objects.get(pk=1020)

    return render(request,'enroll/studetails.html',{'stu' : stu})


def showformdata(request):
    fm = StudentRegistration()
    # fm.order_fields(field_order=['email','name'])
    # fm = StudentRegistration(auto_id=True,label_suffix=' ',initial={'name' : 'Niten'})
    return render(request,'enroll/registeruser.html',{'form' : fm}) 