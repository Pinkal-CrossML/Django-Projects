from Doc_app.models import Document
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from . forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils import timezone


        
@login_required
def save(request):
    form = DocumentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user=request.user.id
            print(user)
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_day_limit=Document.objects.filter(user=user_obj.pk).filter(uploaded_at__date=timezone.now()).count()
            print(pdf_day_limit)
            # breakpoint()
            if pdf_day_limit==5:
                messages.info(request,"you have reached the daily limit wait unitill 12 pm to upload more")
                return redirect('upload')
            else:    
                if form.is_valid():
                    new_doc=Document.objects.create(
                        user_id=user,
                        description=form.cleaned_data['description'],
                        document=form.cleaned_data['document'],
                    )
                    new_doc.save()
                    return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'Doc_app/base.html', {
        'form': form
    })


def index(request):
    form=DocumentForm
    return render(request, 'Doc_app/login.html', {
        'form': form
    })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('upload')
        else:
            messages.error(request,'Invalid Credantials')
            return redirect('index')
    else:
        return render(request,'Doc_app/login.html')

def upload_page(request):
    form=DocumentForm
    return render(request, 'Doc_app/upload.html', {
        'form': form
    })
    

   

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
           
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                

            else:
                user = User.objects.create_user( password=password1, username=username, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User is successfully registered!')
                return redirect('index')
        else:
            messages.error(request,'Password did not match!')
        return redirect('register')
    else:
        return render(request,'Doc_app/register.html')
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,'You have been logout!!')
    return redirect("index")

def contact(request):
    return render(request,'Doc_app/contact.html')
