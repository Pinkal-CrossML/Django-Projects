from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import expense_view
  
urlpatterns = [
    path('', expense_view ),
]