from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
    return render(request,'reward/add_reward.html')

def artists(request):
   form=ArtistForm
   if request.method=='POST':
       add_artist=ArtistForm(request.POST)
       if add_artist.is_valid():
           add_artist.save()
           return render(request,'reward/artists.html',{'form':form})
        
   return render(request,'reward/artists.html',{'form':form})

def awards(request):
    form=AwardForm
    if request.method=='POST':
       add_awards=AwardForm(request.POST)
       if add_awards.is_valid():
           add_awards.save()
           return render(request,'reward/awards.html',{'form':form})
    
    return render(request,'reward/awards.html',{'form':form})

def movies(request):
    form=MovieForm
    if request.method=='POST':
       add_movies=MovieForm(request.POST)
       if add_movies.is_valid():
           add_movies.save()
           return render(request,'reward/movies.html',{'form':form})
    
    return render(request,'reward/movies.html',{'form':form})

def rating(request):
    form=RatingForm
    if request.method=='POST':
       add_rating=RatingForm(request.POST)
       if add_rating.is_valid():
           add_rating.save()
           return render(request,'reward/rating.html',{'form':form})

    return render(request,'reward/rating.html',{'form':form})
