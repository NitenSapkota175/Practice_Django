from django.shortcuts import render,HttpResponse
from datetime import date,time
from school.models import Student  # Adjust the import according to your project structure
def home(request):
    
        # student_data = Student.objects.all()
        # student_data = Student.objects.filter(name__exact='Sumitra Sapkota')
        # student_data = Student.objects.filter(name__iexact='Sumitra Sapkota')
        # student_data = Student.objects.filter(name__contains='i')
        # student_data = Student.objects.filter(name__icontains='i')
        # student_data = Student.objects.filter(id__in=[1,5,7])
        # student_data = Student.objects.filter(marks__in = [60,72,80])
        # student_data = Student.objects.filter(marks__gt=80)
        # student_data = Student.objects.filter(marks__lt=80)
        # student_data = Student.objects.filter(marks__lte=80)
        # student_data = Student.objects.filter(name__startswith='S')
        # student_data = Student.objects.filter(name__istartswith='S')
        # student_data = Student.objects.filter(name__endswith='l')
        # student_data = Student.objects.filter(name__iendswith='l')
        # student_data = Student.objects.filter(passdate__range=('2023-04-01','2023-4-10'))
        # student_data = Student.objects.filter(admdatetime__date=date(2023,4,19)) ## date() it will only work in datetime feild
        # student_data = Student.objects.filter(admdatetime__date__gt=date(2023,4,19)) #both date and datetime
        # student_data = Student.objects.filter(passdate__year=2023) 
        # student_data = Student.objects.filter(passdate__year__gte=2023)
        # student_data = Student.objects.filter(admdatetime__month=4) #both date and datetime
        # student_data = Student.objects.filter(passdate__date__gt=4)
        # student_data = Student.objects.filter(passdate__month_gte=4)
        # student_data = Student.objects.filter(passdate__month_gte=4)

        # student_data = Student.objects.filter(passdate__week=14)  # it will render 14th week data and #both date and datetime

        # student_data = Student.objects.filter(passdate__week_day=5) # here day is day 1 and #both date and datetime

        # student_data = Student.objects.filter(passdate__quarter=2) #this works with date and datetime field both

        # student_data = Student.objects.filter(admdatetime__time__gte=time(6,00)) #datetime

        # student_data = Student.objects.filter(admdatetime__hour__gte=5)       #datetime
        # student_data = Student.objects.filter(admdatetime__minute__gte=26)     #datetime

        # student_data = Student.objects.filter(admdatetime__second__gte=20) #datetime

        student_data = Student.objects.filter(admdatetime__roll_isnull=False)


        print('Return : ',student_data)
        print()
        print('SQL Query : ',student_data.query)
        return render(request,'school/home.html',{ 'students' : student_data})