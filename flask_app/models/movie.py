from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Movie:
    db_name = "movie_project_schema"

    def __init__(self, data ):
        self.id = data["id"]
        self.title = data["title"]
        self.year = data["year"]
        self.plot = data["plot"]
        self.stars = data["stars"]
        self.directors = data["directors"]
        self.awards = data["awards"]
        self.image = data["image"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def add_movies(cls, data):
        query ="""
        INSERT INTO movies(title, year, plot, stars, 
        directors, awards, image) VALUES (%(title)s,%(year)s,
        %(plot)s,%(stars)s,%(directors)s,%(awards)s,%(image)s);
        """
        print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    
