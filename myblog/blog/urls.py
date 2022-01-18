from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('blog/',views.blogs,name='blog'),
    path('blog_details/<int:id>',views.blog_details,name='blog_details'),
]


    
