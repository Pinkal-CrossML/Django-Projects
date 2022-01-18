from django import forms, http
from django.shortcuts import render
from django.urls.resolvers import _route_to_regex
from django.http import HttpResponse, HttpResponseRedirect, request

from .forms import Entry, EntryForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.



def home(request):
    form = EntryForm
    if request.method=='POST':
       form=EntryForm(request.POST or None)
       if form.is_valid():
           form.save()
           msg = "data instert successfully"
           return render(request, "home.html",{'form':form,'msg':msg})
           
    return render(request, "home.html",{'form':form})

    


def show(request):
    data = Entry.objects.all()
    return render(request, "show.html", {'data': data})

def delete(request, pk):
    data = Entry.objects.filter(id =pk)
    if data:
        data.delete()
    return HttpResponseRedirect(reverse('Home:all_records'))
    
        
def entry_edit(request,pk):
    data = Entry.objects.filter(id =pk)
    if data:
        ob = data.get()
        form = EntryForm(request.POST or None, instance=ob)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submission successful')
                return HttpResponseRedirect(reverse('Home:all_records'))
        return render(request, "edit.html",{'ob':ob,'form':form})



