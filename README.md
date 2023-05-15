# Full Stack Final Project

## Introduction / Motivation
This is the final project in completing Udacity's 'Full Stack NanoDegree'. This project covers:
- Database modeling using PostgreSQL and SQLAlchemy which can be seen in the models.py file
- An API to complete CRUD operations as seen in the app.py file
- Automated tests using Unittest that can be seen in the test_app.py file
- Authorization for three different users using Auth0 which can be seen in the auth.py file

## Running the project locally

In order to run the server a few steps need to be followed:

1. install the needed dependencies

first make sure you are in the correct directory and run:

pip install -r requirements.txt

2. update config.py to connect to local database

- open the config.py file and locate the variable 'SQLALCHEMY_DATABASE_URI'
- replace it with your url using the following format: "postgres://{username}:{password}@{host_and_port}/{database_name}"

3. start a virtual environment

.\venv\Scripts\activate

4. we can now run the development server
 
flask run

### Heroku

https://fsndcapstone.herokuapp.com/

## API Documentation

### GET /actors

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key actors, that contains the objects of id, name, age and gender

### GET /movies

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key movies, that contains the objects of id, title and release_date

### DELETE /actors/<int:id>

- Deletes a specified actor using the id of the actpr
- Request Arguments: id - integer
- Returns: the success response and deleted actor id

### DELETE /movies/<int:id>

- Deletes a specified movie using the id of the movie
- Request Arguments: id - integer
- Returns: the success response and deleted movie id

### POST /actors

- Sends a post request in order to add a new actor
- Request body:
- Returns: the success response and the new actor id


### POST /movies

- Sends a post request in order to add a new movie
- Request body:
- Returns: the success response and the new movie id

### PATCH /actors/<actor_id>

- Edits/updates a specifics actors data in the database
- Request Arguments: id - integer
- Returns: the success response and updated actor id

### PATCH /movies/<movie_id

- Edits/updates a specifics movies data in the database
- Request Arguments: id - integer
- Returns: the success response and updated movie id

## Authentication

### Existing Roles
They are 3 Roles with distinct permission sets:

# Casting Assistant:
view:actors: Can see all actors
view:movies: Can see all movies
# Casting Director (everything from Casting Assistant and)
create:actors: Can create new Actors
edit:actors: Can edit existing Actors
delete:actors: Can remove existing Actors from database
edit:movies: Can edit existing Movies
# Exectutive Dircector (everything from Casting Director and)
create:movies: Can create new Movies
delete:movies: Can remove existing Motives from database
