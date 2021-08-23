from django.contrib import admin
from .models import ExpenseCategories, Expense
# Register your models here.

admin.site.register(ExpenseCategories)
admin.site.register(Expense)
