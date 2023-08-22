from flask import render_template, request, redirect, session, json
from flask_app import app
from flask_app.models import movie
import requests, os





@app.route("/")
def home_page():
    return render_template("index.html")



@app.route('/search_movie', methods=['GET', 'POST'])
def search_movie():
    if request.method == 'POST':
        search_query = request.form['search_query']
        url = f"https://imdb-api.com/en/API/Searchmovie/{os.environ.get('IMDB_API_KEY')}/{search_query}"
        response = requests.get(url)

        if response.status_code == 200:
            search_results = response.json()['results']
            # print("Response from IMDB API:", search_results)
            return render_template('index.html', search_results=search_results)
        else:
            return render_template('index.html', search_results=None)
    else:
        return render_template('index.html', search_results=None)
    


@app.route("/add_movie/<imdb_id>", methods=["GET"])
def add_movie(imdb_id):
    if request.method =="GET":
        url = f"https://imdb-api.com/en/API/Title/{os.environ.get('IMDB_API_KEY')}/{imdb_id}"
        print("API URL:", url)
        response = requests.get(url)
        if response.status_code == 200:
            title = response.json() 
            print("Response from IMDB API:", title["stars"])
            data={
                # I use title(response.json)as a list and put the indexes that i want to g
                "title" : title["title"],
                "year" : title["year"],
                "plot" : title["plot"],
                "stars" : title["stars"],
                "directors" : title["directors"],
                "awards" : title["awards"],
                "image" : title["image"],
            }
            movie.Movie.add_movies(data)
            # print(data)
            return render_template("add.html", title=title)
        else:
            return render_template("add.html")
    return redirect("/")



@app.route("/all_favorites", methods=["GET", "POST"])
def all_movies():
    return render_template("all_movies.html", all_movies = movie.Movie.get_all_movies())



@app.route("/delete_movie/<imdb_id>", methods=["POST"])
def delete_movie(imdb_id):
        movie.Movie.delete_movie(imdb_id)
        return redirect("/all_favorites")






















