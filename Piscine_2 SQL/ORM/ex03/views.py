from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


# Create your views here.
def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    results = []

    for movie in data:
        try:
            Movies.objects.create(
                episode_nb=movie[0],
                title=movie[1],
                director=movie[2],
                producer=movie[3],
                release_date=movie[4]
            )
            results.append(f"OK: {movie[1]}")
        except Exception as e:
            results.append(f"Error: {movie[1]} - {str(e)}")

    return HttpResponse("<br>".join(results))


def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available")
        
        table = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            table += f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td><td>{movie.opening_crawl or ''}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
        table += "</table>"
        return HttpResponse(table)
    
    except Exception:
        return HttpResponse("No data available")
