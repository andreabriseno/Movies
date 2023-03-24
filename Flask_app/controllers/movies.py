from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/movie/create')
def create():
    return render_template("createmovie.html")

@app.route('/movie/created', methods=['POST'])
def add():
    data = {
        "title": request.form["title"],
        "genre": request.form["genre"],
        "user_id": session["user_id"]
    }
    Movie.create
    return redirect('/dashboard')