from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('upload',views.upload_page,name='upload'),
    path('save',views.save,name='save'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    
]