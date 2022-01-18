from django.urls import path
from . import views
app_name = 'Home'
urlpatterns = [
    path('',views.home, name="home"),
    path('all',views.show, name="all_records"),
    path('delete/<pk>/',views.delete, name="entry_delete"),
    path('edit/<pk>/',views.entry_edit,name="entry_edit")
]
