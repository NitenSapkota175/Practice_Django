
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.set_session),
    path('get/',views.get_session),
    path('del/',views.delsession)
]
