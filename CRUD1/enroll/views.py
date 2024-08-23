from django.shortcuts import render,HttpResponseRedirect
from . forms import StudentRegistration
from . models import User

def addandshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data.get('name')
            em = fm.cleaned_data.get('email')
            passw = fm.cleaned_data.get('password')
            reg = User(name=nm,email=em,password=passw)
            reg.save()
            fm = StudentRegistration()
    else:
        
        fm = StudentRegistration()
    stud = User.objects.all()


    return render(request,'enroll/addandshow.html',{'form' : fm , "stu" : stud})


def update(request,pk):

    if request.method == 'POST':
        pi = User.objects.get(id=pk)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

    else:
        pi = User.objects.get(id=pk)
        fm = StudentRegistration(instance=pi)

    return render(request,'enroll/update.html',{"form" : fm})


def delete(request,pk):

    if request.method == 'POST':
        pi = User.objects.get(id=pk)
        pi.delete()
        return HttpResponseRedirect('/')

    return render(request,'enroll/addandshow.html')