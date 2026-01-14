import csv
import os
import io

from django.http import HttpResponse
from django.db import connection


# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    climate VARCHAR(128),
                    diameter INTEGER,
                    orbital_period INTEGER,
                    population BIGINT,
                    rotation_period INTEGER,
                    surface_water REAL,
                    terrain VARCHAR(128)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    birth_year VARCHAR(32),
                    gender VARCHAR(32),
                    eye_color VARCHAR(32),
                    hair_color VARCHAR(32),
                    height INTEGER,
                    mass REAL,
                    homeworld VARCHAR(64),
                    FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
                )
            """)
        
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def populate(request):
    results = []
    
    try:
        with connection.cursor() as cursor:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            
            planets_csv = os.path.join(base_dir, 'data', 'planets.csv')
            try:
                with open(planets_csv, 'r') as f:
                    # Skip header
                    next(f)
                    # Use copy_from for bulk insert
                    cursor.copy_from(
                        f,
                        'ex08_planets',
                        sep=',',
                        columns=('id', 'name', 'climate', 'diameter', 'orbital_period', 
                                'population', 'rotation_period', 'surface_water', 'terrain')
                    )
                results.append("OK: All planets inserted")
            except Exception as e:
                results.append(f"Error: Planets - {str(e)}")
            
            people_csv = os.path.join(base_dir, 'data', 'people.csv')
            try:
                with open(people_csv, 'r') as f:
                    # Skip header
                    next(f)
                    # Use copy_from for bulk insert
                    cursor.copy_from(
                        f,
                        'ex08_people',
                        sep=',',
                        columns=('id', 'name', 'birth_year', 'gender', 'eye_color', 
                                'hair_color', 'height', 'mass', 'homeworld')
                    )
                results.append("OK: All people inserted")
            except Exception as e:
                results.append(f"Error: People - {str(e)}")
        
        return HttpResponse("<br>".join(results))
    
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.name, pl.name as homeworld, pl.climate
                FROM ex08_people p
                LEFT JOIN ex08_planets pl ON p.homeworld = pl.name
                WHERE pl.climate LIKE '%windy%' OR pl.climate LIKE '%Windy%'
                ORDER BY p.name ASC
            """)
            rows = cursor.fetchall()
            
            if not rows:
                return HttpResponse("No data available")
            
            table = "<table border='1'><tr><th>Character Name</th><th>Homeworld</th><th>Climate</th></tr>"
            for row in rows:
                table += f"<tr><td>{row[0]}</td><td>{row[1] or 'Unknown'}</td><td>{row[2] or 'Unknown'}</td></tr>"
            table += "</table>"
            
            return HttpResponse(table)
    except Exception:
        return HttpResponse("No data available")
