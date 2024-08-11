from django.contrib import admin
from django.urls import path,include
from course import views as cvs
from fee import views as fvs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn_django/',cvs.learn_django),
    path('fee/',fvs.fee_structure)
]
