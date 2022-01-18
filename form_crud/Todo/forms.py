from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Todolist

class DateInput(forms.DateInput):
    input_type='date'

class TodoForm(ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'
        widgets={
            'date':DateInput()
        }