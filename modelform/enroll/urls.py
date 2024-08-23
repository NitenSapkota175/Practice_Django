from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name="Home"),        
        path('stu/',views.student_details,name="stu"),
        path('register/',views.showformdata,name="register"),
        path('editstut/<int:pk>',views.updatestudent,name="editstu"),
        # path('success/',views.success,name="success")
]