from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex06_movies (
                    episode_nb SERIAL PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL,
                    created TIMESTAMP DEFAULT NOW(),
                    updated TIMESTAMP DEFAULT NOW()
                )
            """)
            
            # Create function for timestamp update
            cursor.execute("""
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
                END;
                $$ language 'plpgsql'
            """)
            
            # Create trigger and fix indempotency issue
            cursor.execute("""
                DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies
            """)
            
            cursor.execute("""
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column()
            """)
            
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


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
                        INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (episode_nb) DO NOTHING
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
            cursor.execute("SELECT episode_nb, title, opening_crawl, director, producer, release_date, created, updated FROM ex06_movies ORDER BY episode_nb")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")
            table = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Created</th><th>Updated</th></tr>"
            for row in rows:
                table += "<tr>" + "".join(f"<td>{cell if cell is not None else ''}</td>" for cell in row) + "</tr>"
            table += "</table>"
            return HttpResponse(table)
    except Exception:
        return HttpResponse("No data available")


def update(request):
    try:
        with connection.cursor() as cursor:
            if request.method == "POST":
                title_to_update = request.POST.get("title")
                new_opening_crawl = request.POST.get("opening_crawl")
                try:
                    cursor.execute(
                        "UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s",
                        [new_opening_crawl, title_to_update]
                    )
                except Exception as e:
                    return HttpResponse(f"Error: {str(e)}")

            cursor.execute("SELECT title FROM ex06_movies ORDER BY episode_nb")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")

            options = "".join(f"<option value='{row[0]}'>{row[0]}</option>" for row in rows)
            form = f"""
                <form method="POST">
                    {{% csrf_token %}}
                    <select name="title">{options}</select>
                    <br><br>
                    <textarea name="opening_crawl" rows="5" cols="50"></textarea>
                    <br><br>
                    <button type="submit">Update</button>
                </form>
            """
            return HttpResponse(form)
    except Exception as e:
        return HttpResponse("No data available")
