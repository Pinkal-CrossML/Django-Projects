from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def home(request):
    blog = Blog.objects.order_by('-id')[:3]
    context = {'blogs':blog}
    return render(request,'pages/home.html',context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')


