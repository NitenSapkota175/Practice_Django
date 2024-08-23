from django.shortcuts import render
from . forms import StudentRegistration


def addandshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
    else:
        
        fm = StudentRegistration()


    return render(request,'enroll/addandshow.html',{'form' : fm})


def update(request,pk):
    return render(request,'enroll/update.html')


def delete(request,pk):
    return render(request,'enroll/addandshow.html')