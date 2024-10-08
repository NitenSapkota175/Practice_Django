from django.shortcuts import render
from django.contrib import messages
from . forms import StudentRegistration

def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,"your account has been created")
            messages.success(request,'Your account has been created')

    else:
        fm = StudentRegistration()
    return render(request,'enroll/registration.html',{'forms' : fm })