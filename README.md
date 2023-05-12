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

3. we can now run the development server using:

flask run
