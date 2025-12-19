from django.shortcuts import render
from .models import Movies


# Create your views here.
def movies_list(request):
    movies = Movies.objects.all()
    return render(request, 'ex01/movies_list.html', {'movies': movies})