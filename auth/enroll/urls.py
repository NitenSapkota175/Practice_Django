from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.user_profile,name='profile'),
    path('signup/' , views.sign_up,name="signup"),
    path('login/' , views.user_login,name="login"),
    path('logout/' , views.user_logout,name="logout"),
    path('changepass/',views.user_change_pass,name="changepass"),
    path('changepass1/',views.user_change_pass1,name="changepass1")
   
]
