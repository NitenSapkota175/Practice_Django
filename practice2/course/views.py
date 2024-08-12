from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def learn_django(request):
   # d = datetime.now()
   # fl = 67.81237829
   # context = {"name" : "learn django with me" , "duration" : "2 months ", "try" : False, 'd' : d,'fl' : fl}
   # context = {'nm' : "Django" , "st" : 5}

   stud = {


      "stud1" : {"name" : "Niten" , 'roll' : 101},
      "stud2" : {"name" : "Bishesh" , 'roll' : 102},
      "stud3" : {"name" : "Ashwini" , 'roll' : 103},
      "stud4" : {"name" : "Sahil" , 'roll' : 104}

      
      }
   
   students = {'student' : stud}

   return render(request,'course/course.html' ,students )


