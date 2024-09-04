from django.shortcuts import render

from . models import Student,ExamCenter
# Create your views here.
def home(request):
    students_data = Student.objects.all()
    examCenter_data = ExamCenter.objects.all()
    context = {'students' : students_data , 'examcenters' : examCenter_data }
    return render(request,'school/home.html',context)