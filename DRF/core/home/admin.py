from django.contrib import admin

from home.models import Student

# Register your models here.
from .models import *
admin.site.register(Student)