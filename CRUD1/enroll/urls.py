from django.urls import path,include
from . import views
urlpatterns = [
            path('' , views.addandshow,name="addandshow"),
            path('updatestu/<int:pk>/' , views.update,name="updatestu"),
            path('deletestu/<int:pk>/' , views.delete,name="deletestu")
]
