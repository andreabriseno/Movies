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


    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO 
                movie
                    (title, 
                    genre, 
                    users_id) 
            VALUES 
                (%(title)s, 
                %(genre)s,
                %(users_id)s);
            """
        results = connectToMySQL(DB).query_db(query, data)
        return results
    
    @classmethod
    def destroy (cls, data):
        query = "DELETE FROM events WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)