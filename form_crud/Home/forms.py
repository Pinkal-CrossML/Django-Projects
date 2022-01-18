from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'