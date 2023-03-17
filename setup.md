-MySQL WorkBench
-Activating shell pipenv shell
-Flask pipenv install flask
-Checking whats installed pip list 
-PyMySQL pipenv install PyMySQL flask
-Flask-Bcrypt pipenv install flask-bcrypt
Database 
    -Create ERD in Workbench: Platform
    -Making sure to choose AI for the id field for all tables included
    -Forward Engineer
    -Save ERD Model to Project Folder
    -(Optional) Create screenshot of ERD and save to project folder
Application 
1. Create Folder for the application (Movie-App)
2. Create folder inside application folder called Flask-App
3. Create server.py inside application app
4. Create __init__.py inside flask_app
5. Inside flask_app folder create the following folders:
        templates: will hold all html files
        static: will hold css, js and images (typicaly in their own respective folders)
        config: will hold the mysqlconnection.py file Platform file
        models: will hold all the model files (each file called by their table name (user.py, movie.py)): Platform
        controllers: Will contain the controller/routing files (each named after their table name but plural (users.py, movies.py)): 