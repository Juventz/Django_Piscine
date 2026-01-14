from django.http import HttpResponse
from django.shortcuts import render

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
				release_date=movie[4],
			)
			results.append(f"OK: {movie[1]}")
		except Exception as exc:
			results.append(f"Error: {movie[1]} - {exc}")

	return HttpResponse("<br>".join(results))


def display(request):
	try:
		movies = Movies.objects.all().order_by("episode_nb")
		if not movies:
			return HttpResponse("No data available")

		table = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Created</th><th>Updated</th></tr>"
		for movie in movies:
			table += (
				"<tr>"
				f"<td>{movie.episode_nb}</td>"
				f"<td>{movie.title}</td>"
				f"<td>{movie.opening_crawl or ''}</td>"
				f"<td>{movie.director}</td>"
				f"<td>{movie.producer}</td>"
				f"<td>{movie.release_date}</td>"
				f"<td>{movie.created}</td>"
				f"<td>{movie.updated}</td>"
				"</tr>"
			)
		table += "</table>"
		return HttpResponse(table)
	except Exception:
		return HttpResponse("No data available")


def update(request):
	try:
		if request.method == "POST":
			title_to_update = request.POST.get("title")
			new_opening_crawl = request.POST.get("opening_crawl")
			try:
				Movies.objects.filter(title=title_to_update).update(opening_crawl=new_opening_crawl)
			except Exception as exc:
				return HttpResponse(f"Error: {exc}")

		titles = Movies.objects.all().order_by("episode_nb").values_list("title", flat=True)
		if not titles:
			return HttpResponse("No data available")

		options = "".join(f"<option value='{title}'>{title}</option>" for title in titles)
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
	except Exception:
		return HttpResponse("No data available")
