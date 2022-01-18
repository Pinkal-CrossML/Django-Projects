from django.urls import path
from . import views
app_name = 'Todo'

urlpatterns = [
    path('',views.show, name="todo"),
    path('all',views.todoshow, name="all_records"),
    path('delete/<pk>/',views.delete, name="entry_delete"),
    path('edit/<pk>/',views.entry_edit,name="entry_edit"),
]