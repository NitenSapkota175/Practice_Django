from django.contrib import admin

from .models import Student

#using decorator 


@admin.register(Student)
class StudentAdim(admin.ModelAdmin):
    list_display = ('id','stuid','stuname','stuemail','stupass')



# admin.site.register(Student,StudentAdim)
