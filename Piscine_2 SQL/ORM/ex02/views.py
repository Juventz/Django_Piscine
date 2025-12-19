from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS ex02_movies (
                               title VARCHAR(64) UNIQUE NOT NULL,
                               episode_nb SERIAL PRIMARY KEY,
                               opening_crawl TEXT,
                               director VARCHAR(32) NOT NULL,
                               producer VARCHAR(128) NOT NULL,
                               release_date DATE NOT NULL
                            )
                        """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


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

    try:
        with connection.cursor() as cursor:
            for movie in data:
                try:
                    cursor.execute("""
                        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s)
                    """, movie)
                    results.append(f"OK: {movie[1]}")
                except Exception as e:
                    results.append(f"Error: {movie[1]} - {str(e)}")

        return HttpResponse("<br>".join(results))
    
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ex02_movies")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")
            table = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
            for row in rows:
                table += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
            table += "</table>"
        return HttpResponse(table)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def clear_table(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS ex02_movies")
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
