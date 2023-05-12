import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db, Actors, Movies
from auth import AuthError, requires_auth

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  db_drop_and_create_all()
  return app

app = create_app()

CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

# ENDPOINTS

# GET /actors and /movies

@app.route('/actors')
@requires_auth('get:actors')
def get_actors():
  try:
    actors = Actors.query.all()
    return jsonify({
        "success": True,
        "actors": actors
      })
  except Exception as e:
            print(e)
            abort(500)

@app.route('/movies')
@requires_auth('get:movies')
def get_movies():
  try:
    movies = Movies.query.all()
    return jsonify({
        "success": True,
        "movies": movies
      })
  except Exception as e:
            print(e)
            abort(500)

# DELETE /actors/ and /movies/

@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(id):
    actors = Actors.query.filter(Actors.id == id).one_or_none()
    if (actors is None):
        abort(400)
    try:
        actors.delete()
        return jsonify({
            "success": True,
            "deleted": actors.id})
    except Exception as e:
        print(e)
        abort(500)

@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(id):
    movies = Movies.query.filter(Movies.id == id).one_or_none()
    if (movies is None):
        abort(400)
    try:
        movies.delete()
        return jsonify({
            "success": True,
            "deleted": movies.id})
    except Exception as e:
        print(e)
        abort(500)

# POST /actors and /movies

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actors():
    data = request.get_json()

    if data is None:
        abort(400)

    new_name = data['name']
    new_age = data['age']
    new_gender = data['gender']

    new_actor = (Actors(name=new_name, age=new_age, gender=new_gender))
    new_actor.insert()

    return jsonify({
      'success': True,
      'created': new_actor.id
    })

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movies():
    data = request.get_json()

    if data is None:
        abort(400)

    new_title = data['title']
    new_release_date = data['release_date']

    new_movie = (Movies(title=new_title, release_date=new_release_date))
    new_movie.insert()

    return jsonify({
      'success': True,
      'created': new_movie.id
    })

# PATCH /actors/ and /movies/

@app.route('/actors/<actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actors(actor_id):
    data = request.get_json()

    if data is None:
        abort(400)

    update_actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

    if not update_actor:
        abort(404)

    update_actor.name = data['name']
    update_actor.age = data['age']
    update_actor.gender = data['gender']

    update_actor.update()

    return jsonify({
        'success': True,
        'updated': update_actor.id
    })

@app.route('/movies/<movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movies(movie_id):
    data = request.get_json()

    if data is None:
        abort(400)
    
    update_movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

    if not update_movie:
        abort(404)
    
    update_movie.title = data['title']
    update_movie.release_date = data['release_date']

    update_movie.update()

    return jsonify({
        'success': True,
        'updated': update_movie.id
    })

# error handling

@app.errorhandler(400)
def bad_request(error):
        return jsonify({
            "success": False,
            'error': 400,
            "message": "Bad request"
        }), 400

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        'error': 404,
        "message": "Page not found"
    }), 404

@app.errorhandler(422)
def unprocessable_recource(error):
    return jsonify({
        "success": False,
        'error': 422,
        "message": "Unprocessable recource"
    }), 422

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        'error': 500,
        "message": "Internal server error"
    }), 500

@app.errorhandler(405)
def invalid_method(error):
    return jsonify({
        "success": False,
        'error': 405,
        "message": "Invalid method!"
    }), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)