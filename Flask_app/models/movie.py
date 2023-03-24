from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

DB= "movies"

class Movie:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM movie;"
        results = connectToMySQL(DB).query_db(query)
        movie = []
        for m in results:
            movie.append(cls(m))
        return movie

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO 
                movie
                    (title, 
                    genre, 
                    user_id) 
            VALUES 
                (%(title)s, 
                %(genre)s,
                %(user_id)s);
            """
        results = connectToMySQL(DB).query_db(query, data)
        return results
    
    @classmethod
    def destroy (cls, data):
        query = "DELETE FROM movie WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)