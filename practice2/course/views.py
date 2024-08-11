from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
   context = {"name" : "django" , "duration" : "2 months "}
   return render(request,'course/course.html',context)

