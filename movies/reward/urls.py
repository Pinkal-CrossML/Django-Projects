from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists', views.artists, name='artists'),
    path('awards', views.awards, name='awards'),
    path('movies', views.movies, name='movies'),
    path('rating', views.rating, name='rating'),
    
    ]