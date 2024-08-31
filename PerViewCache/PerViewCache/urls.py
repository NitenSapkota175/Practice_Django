from django.contrib import admin
from django.urls import path
from enroll import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cache_page(60)(views.home)),  #only for this specific url #this is the good practice
    path('contact/',views.contact)
]
