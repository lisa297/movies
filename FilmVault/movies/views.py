from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse

def movie_list(request):
    movies = Movie.objects.all()
    return render(request,'movies/movie_list.html', {'movies': movies})

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request,'movies/movie_details.html',{'movie': movie})
