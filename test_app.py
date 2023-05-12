import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actors, Movies
from datetime import date

casting_assistant_auth_header = {
    'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx4MWtINlNIdnh1SEpXZ1k3SUxfdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycTZ6Zm10M3BodTUyY29tLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDVhNjg4ODgzMDE1YTk2ODdkYWFlODgiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4Mzg5MDI3OCwiZXhwIjoxNjgzODk3NDc4LCJhenAiOiJFZ3hJQ1ltTVVmMVYwdWdjVmpTZlJVUVFHMDVLNjVoTCIsInNjb3BlIjoiIn0.hpACwXrUIlg1zM7lXThVM2EZgW-fORba230r5R-sRHEOqH_2K1SlR1EegjWKWo9R9y7Z2A9pVwXCg_0nVV7kt11j4nTj67DZvN5hvyEd3_2w0U7fQcx6sk4Glm7sbqxpC-lqjwRtbbh1-XD9S-gh6KdisKq9Kyi1njlbpiUQsUolTPgArfx0H4CH6E_xLvp23F4Y1WJ6HrX7l2TR9RSlyy-vkfz623GRLuPElOI092AdKHqfsshc9V07KyBGMsG8piLYSfc6OWKi_W3p7NCgkzG3h9DkqEOpLDQTsJERwnV1toWpb1I65UTcXSotKCa0Q18hdFnXnIEbALTM0FVt5Q'
}

casting_director_auth_header = {
    'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx4MWtINlNIdnh1SEpXZ1k3SUxfdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycTZ6Zm10M3BodTUyY29tLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDJkNzRhY2MxNTZlODg4M2VjYmU5MmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4Mzg5MDM3NiwiZXhwIjoxNjgzODk3NTc2LCJhenAiOiJFZ3hJQ1ltTVVmMVYwdWdjVmpTZlJVUVFHMDVLNjVoTCIsInNjb3BlIjoiIn0.VuqwVCU9Jb8lrb8FjUzX4ORJhPEijX74w0YAEDXft0NVvKYCL1EYmpu5juRDUrWCx58W1VKYqX-N4o0aYo-Bbdo2YhgziPdDLGzoU4h9oTb8jYQ57Vb4Kme3rOq7Y3DRdSOsyS6NjPEAZOboZ8ZYD_j9WXRa53EnuhgmDu9Rvf6vsZBM1fIF-5VODjJ4Nst0Cwdpn2oD6gsiSo33TdnYTUt1Z_LSdR5HYpem8yIjp2A_zmFdoLWeWg0zhx-kdvUE0pOUVUHx9K1YUdqsIlIKa3COJfk7fpABvTCgZEJs7KqivK_oEeAUdyOHAFe57XRRwBWdfBsGVgiPyX4vPNDllQ' 
}

executive_producer_auth_header = {
    'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx4MWtINlNIdnh1SEpXZ1k3SUxfdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycTZ6Zm10M3BodTUyY29tLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDMyZGJmZTUyZmI3NjdmN2VhZWFkMGEiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4Mzg5MDQ1NiwiZXhwIjoxNjgzODk3NjU2LCJhenAiOiJFZ3hJQ1ltTVVmMVYwdWdjVmpTZlJVUVFHMDVLNjVoTCIsInNjb3BlIjoiIn0.GyRXbwyCcXboQJJoEz5ljP5jYbsruwYS8KB-C-SQI_VJGMofkc2JAX2Y2PJ77EA8ketTbCJZ53y2LsDfhRXrcpjyleUdgnmxGvZQLGONYNLJQuYcd0J_E6WXsqX3gDInV4hwcLCfz9vKBYbubq8j6Dkzw5mvMAwFhP7qUnB4FpqG9Qpu55tY5RhoWtk1JVhvyNIBRdqlyH20BAouO4wumA2-msYePteGvcFN5sl5XnKpxqShCM9eIgsndBazxWe1BFFka80pQGXgNwYeFJaRPsWTWC9lId0UaAJJwEhoRI1Ob6KOS1QDr0vuAnR-5hHG28YSo3zGY86Ru28irIP4rw'
}

class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = 'postgresql://postgres:<PASSWORD>@localhost:5432/Capstone_Test'
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
            
    def tearDown(self):
        pass

    def test_create_new_actor(self):
        json_create_actor = {
            'name' : 'George',
            'age' : 21
        } 

        res = self.client().post('/actors', json=json_create_actor, headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
    
    def test_error_401_new_actor(self):
        json_create_actor = {
            'name' : 'George',
            'age' : 21
        } 

        res = self.client().post('/actors', json=json_create_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_422_create_new_actor(self):
        json_create_actor_without_name = {
            'age' : 23
        } 

        res = self.client().post('/actors', json = json_create_actor_without_name, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_get_all_actors(self):
        res = self.client().get('/actors?page=1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_get_all_actors(self):
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_actors(self):
        res = self.client().get('/actors?page=1125125125', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

    def test_edit_actor(self):
        json_edit_actor_with_new_age = {
            'age' : 19
        } 
        res = self.client().patch('/actors/1', json = json_edit_actor_with_new_age, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_400_edit_actor(self):
            res = self.client().patch('/actors/123412', headers=casting_director_auth_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 400)
            self.assertFalse(data['success'])
            self.assertEqual(data['message'] , 'Bad request')

    def test_error_404_edit_actor(self):
        json_edit_actor_with_new_age = {
            'age' : 19
        } 
        res = self.client().patch('/actors/123412', json = json_edit_actor_with_new_age, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

    def test_error_401_delete_actor(self):
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_actor(self):
        res = self.client().delete('/actors/1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_404_delete_actor(self):
        res = self.client().delete('/actors/15125', headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

    def test_create_new_movie(self):
        json_create_movie = {
            'title' : 'Yourself',
            'release_date' : date.today()
        } 

        res = self.client().post('/movies', json = json_create_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_422_create_new_movie(self):
        json_create_movie_without_name = {
            'release_date' : date.today()
        } 

        res = self.client().post('/movies', json = json_create_movie_without_name, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_get_all_movies(self):
        res = self.client().get('/movies?page=1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_get_all_movies(self):
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_movies(self):
        res = self.client().get('/movies?page=1125125125', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

    def test_edit_movie(self):
        json_edit_movie = {
            'release_date' : date.today()
        } 
        res = self.client().patch('/movies/1', json = json_edit_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_400_edit_movie(self):
        res = self.client().patch('/movies/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Bad request')

    def test_error_404_edit_movie(self):
        json_edit_movie = {
            'release_date' : date.today()
        } 
        res = self.client().patch('/movies/123412', json = json_edit_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

    def test_error_401_delete_movie(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_movie(self):
        res = self.client().delete('/movies/1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_404_delete_movie(self):
        res = self.client().delete('/movies/151251', headers = executive_producer_auth_header) 
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Not found')

        
if __name__ == "__main__":
    unittest.main()
