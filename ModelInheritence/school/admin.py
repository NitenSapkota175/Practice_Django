from django.contrib import admin
from . models import Student,Teacher,Contractor

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','fees']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','salary']


@admin.register(Contractor)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','payment']