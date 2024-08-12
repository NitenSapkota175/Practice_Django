from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def learn_django(request):
   # d = datetime.now()
   # fl = 67.81237829
   # context = {"name" : "learn django with me" , "duration" : "2 months ", "try" : False, 'd' : d,'fl' : fl}
 


   return render(request,'course/course.html' , {'nm' : "Django" , "st" : 5})

