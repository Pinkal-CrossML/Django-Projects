from django.contrib import admin
from django.urls import path,include

from .views import *

from . import views

urlpatterns = [
    path('',show),
    path('create/',post_student),
    path('detail/<str:pk>/', views.Detail, name="Detail"),
    path('update/<str:pk>/',views.Update, name="Update"),
    path('delete/<str:pk>/', views.Delete, name="Delete"),
]
