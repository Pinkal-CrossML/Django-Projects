from django import forms, http
from django.shortcuts import render
from django.urls.resolvers import _route_to_regex
from django.http import HttpResponse, HttpResponseRedirect, request

from Todo.models import Todolist
from .forms import TodoForm
from django.urls import reverse
from django.contrib import messages

def show(request):
    form = TodoForm
    if request.method=='POST':
       form=TodoForm(request.POST or None)
       if form.is_valid():
           form.save()
           msg = "data instert successfully"
           return render(request, "todo.html",{'form':form,'msg':msg})
    
    return render(request, "todo.html",{'form':form})


def todoshow(request):
    data = Todolist.objects.all()
    return render(request, "todo_show.html", {'data': data})



def delete(request, pk):
    data = Todolist.objects.filter(id =pk)
    if data:
        data.delete()
    
    return HttpResponseRedirect(reverse('Todo:all_records'))

def entry_edit(request,pk):
    data = Todolist.objects.filter(id =pk)
    if data:
        ob = data.get()
        form = TodoForm(request.POST or None, instance=ob)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submission successful')
                return HttpResponseRedirect(reverse('Todo:all_records'))
        return render(request, "todo_edit.html",{'ob':ob,'form':form})
    