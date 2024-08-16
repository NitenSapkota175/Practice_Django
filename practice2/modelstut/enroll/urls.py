from django.urls import path
from . import views

urlpatterns = [

        path('stu/',views.student_details,name="stu")
]