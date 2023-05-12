import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# database url
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Delphie06!@localhost:5432/Capstone'
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
