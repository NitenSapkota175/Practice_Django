from django.shortcuts import render
from . models import Student
def home(request):
        # student_data = Student.objects.all()
        # print('Return : ', student_data)
        # print('Query : ', student_data.query)

        # student_data = Student.objects.filter(marks=70) # filter always  returns queryset and the parameter given inside a marks is called lookup parameter 
        # student_data = Student.objects.exclude(marks=70)
        # student_data = Student.objects.order_by('?') ##random
        # student_data = Student.objects.order_by('marks') # asce
        # student_data = Student.objects.order_by('-marks') # desc
        # student_data = Student.objects.order_by('name') # in string it order by the unicode value of characters
        # student_data = Student.objects.order_by('id').reverse()[:5]
        # student_data = Student.objects.values() ## it gives dictionryory list
        # student_data = Student.objects.values('name','city') ## if you want retrive sepcific colums
        # student_data = Student.objects.values_list('id','name',named=True)
        # student_data = Student.objects.using('default') ## this gives you which database you aare working on 
        # student_data = Student.objects.dates('pass_date','month')


    ################################### Second table ##########################################
        # qs1 = Student.objects.values_list('id','name',named=True)
        # qs2 = Student.objects.values_list('id','name',named=True)
        # student_data = qs2.union(qs1)

        # qs1 = Student.objects.values_list('id','name',named=True)
        # qs2 = Student.objects.values_list('id','name',named=True)
        # student_data = qs2.union(qs1 , all=True)

        # qs1 = Student.objects.values_list('id','name',named=True)
        # qs2 = Student.objects.values_list('id','name',named=True)
        # student_data = qs2.intersection(qs1)


        # qs1 = Student.objects.values_list('id','name',named=True)
        # qs2 = Student.objects.values_list('id','name',named=True)
        # student_data = qs1.difference(qs2)

        # qs1 = Student.objects.values_list('id','name',named=True)
        # qs2 = Student.objects.values_list('id','name',named=True)
        # student_data = qs2.intersection(qs1)

        ########################## AND Operator ####################################################

        # student_data = Student.objects.filter(id=5) & Student.objects.filter(roll=106)

        ######### or you can use this instead of and ###############33
        # student_data = Student.objects.filter(id=5 , roll=106)

        ############################# OR  operator ######################################

        # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=106)
        

        return render(request,'school/home.html',{'students' : student_data })