from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.user_profile,name='profile'),
    path('signup/' , views.sign_up,name="signup"),
    path('login/' , views.user_login,name="login"),
    path('logout/' , views.user_logout,name="logout"),
   
]
