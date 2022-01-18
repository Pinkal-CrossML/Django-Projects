from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def blogs(request):
    blog = Blog.objects.order_by('-id')
    context = {'blogs':blog}
   
    return render(request,'blog/blogs.html',context)

# def blog_details(request,id):
#     blog = Blog.objects.get(id=id)
#     context = {'blog': blog}
#     return render(request,'blog/blogdata.html',context)    


def blog_details(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog/blog_details.html',context)