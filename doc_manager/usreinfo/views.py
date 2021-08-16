from django.shortcuts import render
from django.http import HttpResponse
from .models import Userdata

# Create your views here.
def listview(request):
    all_docs = Userdata.objects.all()
    context = {"all_docs":all_docs}

    print(type(all_docs[0]))

    # print(type(docs_list[0]))

    return render(request, 'list.html', context)