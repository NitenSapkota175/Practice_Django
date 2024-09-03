from django.shortcuts import render
from . models import Student
def home(request):
    

    ################################## methods that don't return query set ###############################




    # student_data = Student.objects.get(pk=1)   
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')
    # student_data = Student.objects.all()
    # print(student_data.exists()) # returns true if the query set has a data

    # student_data = Student.objects.create(
    #     name='Jai Prasad Sapkota' , 
    #     roll = 111 , city='SIligur' , 
    #     marks=80,
    #     pass_date='2019-05-04')
   
   
    # student_data , created = Student.objects.get_or_create(
    #     name='Sumitra Chettri' , 
    #     roll = 112 , city='Siliguri' , 
    #     marks=70,
    #     pass_date='2020-05-04')
   
    # print(created)

    # student_data = Student.objects.filter(pk=12).update(name="Sumitra Sapkota") # update is only applied and valid with queryset not query objects that way we use filter insted of get() as filter returns query sets
    # print(student_data)
    # student_data,created = Student.objects.update_or_create(id=12, name="Sumitra Sapkota" , 
    #                                                         defaults = {'name' : 'Sumi Sapkota'}) , here if the data is to be created then you need to add all the not null fields 
    # print(created)
   
    
    # objs = [
    #     Student(name='Aashok Chettri',roll = 113,city='Siliguri',marks=40,pass_date='2019-03-04'),
    #     Student(name='Bimal Chettri',roll = 114,city='Siliguri',marks=50,pass_date='2018-08-04'),
    #     Student(name='Sanju Chettri',roll = 115,city='Siliguri',marks=80,pass_date='2016-12-04'),
    # ]

    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()

    # for stu in all_student_data:
    #     stu.city = 'Bhel'
    # student_data = Student.objects.bulk_update(all_student_data,['city'])

    # student_data = Student.objects.in_bulk([3,2])
    # print(student_data[2].name)

    # student_data = Student.objects.in_bulk([])
    # print(student_data)


    # student_data = Student.objects.in_bulk()
    # print(student_data)

    
    # student_data = Student.objects.get(pk=14).delete()
    # print(student_data)


    # student_data = Student.objects.get(marks=50).delete()
    # print(student_data)

    # student_data = Student.objects.all().delete()
    # print(student_data)

    student_data = Student.objects.all().count()
    print(student_data)







    return render(request,'school/home.html',{'stu' : student_data })