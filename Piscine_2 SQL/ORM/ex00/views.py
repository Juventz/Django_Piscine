import psycopg2
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.
def init(request):
    try:
        conn = pyscopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432'
        )
        cursor = conn.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) NOT NULL UNIQUE,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
        );
        """

        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()

        return HttpResponse('OK')
    
    except Exception as e:
        return HttpResponse(f"{type(e).__name__}: {e}")