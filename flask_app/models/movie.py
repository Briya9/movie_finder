from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Movie:
    db_name = "movie_project_schema"

    def __init__(self, b ):
        self.imdb_id = b["id"]
        self.id = b["id"]
        self.title = b["title"]
        self.year = b["year"]
        self.plot = b["plot"]
        self.stars = b["stars"]
        self.directors = b["directors"]
        self.awards = b["awards"]
        self.image = b["image"]
        self.created_at = b["created_at"]
        self.updated_at = b["updated_at"]


    @classmethod
    def add_movies(cls, data):
        query ="""
        INSERT IGNORE INTO movies( imdb_id, title, year, plot, stars, 
        directors, awards, image) VALUES (%(id)s,%(title)s,%(year)s,
        %(plot)s,%(stars)s,%(directors)s,%(awards)s,%(image)s);
        """
        # print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    
    @classmethod
    def get_all_movies(cls): 
        query = """
        SELECT * FROM movies ;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        movies = []
        for movie in results:
            movies.append(cls(movie))
        return movies

                

    @classmethod
    def delete_movie(cls, movie_id):
        query="""
        DELETE FROM movies WHERE id=%(id)s;
        """
        data={
            "id":movie_id
        }
        # print (query)
        return connectToMySQL(cls.db_name).query_db(query, data)
            
