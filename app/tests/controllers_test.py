import unittest
from lms import app
from requests.auth import _basic_auth_str
import os
import json
from base64 import b64encode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app.testing = True

class TestControllers(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        host = os.environ['POSTGRES_HOST']
        port = os.environ['POSTGRES_PORT']
        password = os.environ['POSTGRES_PASSWORD']
        schema = os.environ['POSTGRES_SCHEMA']
        cls.db_string = f'postgresql://{schema}:{password}@{host}:{port}/{schema}'
        cls.engine = create_engine(cls.db_string).execution_options(isolation_level="AUTOCOMMIT")
        cls.Session = sessionmaker(bind = cls.engine)
        cls.user_id = "00000000-0000-0000-0000-000000000001"
        res = app.test_client().get("/get-auth-token", headers={"Authorization":_basic_auth_str("00000000-0000-0000-0000-000000000001", "student1")})
        cls.token = json.loads(res.data.decode('ascii'))['token']
        cls.user_id = "00000000-0000-0000-0000-000000000001"
        
    @classmethod
    def tearDownClass(cls):
        # TODO: fix hang ?
        # with cls.engine.connect() as con:
        #     con.execution_options(autocommit=True).execute(text(open(cls.clean_data_path).read()))
        #     con.close()
        pass

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_get_profile(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            result = client.get('/profile/00000000-0000-0000-0000-000000000001')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0000-000000000001":["student1_first_name","student1_middle_name","student1_last_name","student1@example.com","+7-900-111-22-33","Moscow","","vk.com/exmaple","facebook.com/exmaple","instagram.com/exmaple","day"]}\n'
            )

    def test_get_group(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            result = client.get('/groups')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0000-000000000001":["student1_first_name","student1_middle_name","student1_last_name"],"00000000-0000-0000-0000-000000000002":["student2_first_name","student2_middle_name","student2_last_name"]}\n'
            )

    def test_get_courses(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            result = client.get('/courses')
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description"]}\n'
            )

    def test_get_course_info(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            result = client.get('/course/00000000-0000-0000-0004-000000000001')
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description","00000000-0000-0000-0003-000000000004",""]}\n'
            )

    def test_get_solutions(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            result = client.get('/solutions/00000000-0000-0000-0004-000000000001')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0006-000000000001":["00000000-0000-0000-0005-000000000001","00000000-0000-0000-0001-000000000001","00000000-0000-0000-0004-000000000001","description"]}\n'
            )

    def test_register(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = {'registration_code': 'code1'}
            result = client.post('/register', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_auth(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = {'email': 'student1@example.com', 'password': 'student1'}
            result = client.post('/auth', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_post_profile(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = {
                'email': 'student1@example.com',
                'phone_number': '+79001112233',
                'city': 'Moscow',
                'about': 'myself',
                'vk_link': 'https://vk.com/kek',
                'facebook_link': 'https://facebook.com/hh',
                'instagram_link': 'https://instagram.com/hh',
            }
            result = client.post('/profile/00000000-0000-0000-0000-000000000001', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_post_material(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = {
                'material_name': 'material2_name', 
                'material_content': 'material2_name', 
                'add_date': 'material2_name',  
                'course_id': '00000000-0000-0000-0004-000000000001', 
                }
            result = client.post('/material', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )
    
    def test_post_homework(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = { 
                'homeworks_name': 'homework9', 
                'homework_start_date': '19.12.2020', 
                'homework_end_date': '26.12.2020', 
                'description': 'very hard homework', 
                'course_id': '00000000-0000-0000-0004-000000000001'
                }
            result = client.post('/homework', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_post_solution(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'token', self.token)
            client.set_cookie('localhost', 'user_id', self.user_id)
            post_data = { 
                'homework_id': '00000000-0000-0000-0005-000000000001',
                'student_id': '00000000-0000-0000-0001-000000000001',
                'course_id': '00000000-0000-0000-0004-000000000001',
                'description': 'very good solution'
                }
            result = client.post('/solution', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )
