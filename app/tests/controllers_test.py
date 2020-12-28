import json
import time
import unittest
from lms import app

from sqlalchemy import create_engine, text
from sqlalchemy import func, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from lms.model import *


app.testing = True


class TestControllers(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls.db_string = "postgresql://postgres:example@localhost:5432/postgres"
        cls.initdb_path = '/home/care1e55/study/MIPT/architecture/LMS/app/init.sql'
        cls.test_data_path = '/home/care1e55/study/MIPT/architecture/LMS/app/fill_test_data.sql'
        cls.clean_data_path = '/home/care1e55/study/MIPT/architecture/LMS/app/clean_test_data.sql'
        cls.engine = create_engine(cls.db_string).execution_options(isolation_level="AUTOCOMMIT")
        cls.Session = sessionmaker(bind = cls.engine)

        with cls.engine.connect() as connection:
            try:
                connection.execute(text(open(cls.initdb_path).read()))
                connection.execute(text(open(cls.test_data_path).read()))
            except:
                pass
            connection.close()
        

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
            result = client.get('/profile/00000000-0000-0000-0000-000000000001')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0000-000000000001":["student1_first_name","student1_middle_name","student1_last_name","student1@example.com","+7-900-111-22-33","Moscow","","vk.com/exmaple","facebook.com/exmaple","instagram.com/exmaple","day"]}\n'
            )

    def test_get_group(self):
        with app.test_client() as client:
            result = client.get('/groups/00000000-0000-0000-0000-000000000001')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0000-000000000001":["student1_first_name","student1_middle_name","student1_last_name"],"00000000-0000-0000-0000-000000000002":["student2_first_name","student2_middle_name","student2_last_name"]}\n'
            )

    def test_get_courses(self):
        with app.test_client() as client:
            result = client.get('/courses/00000000-0000-0000-0000-000000000001')
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description"]}\n'
            )

    def test_get_course_info(self):
        with app.test_client() as client:
            result = client.get('/course/00000000-0000-0000-0004-000000000001')
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description","00000000-0000-0000-0003-000000000004",""]}\n'
            )

    def test_get_solutions(self):
        with app.test_client() as client:
            result = client.get('/solutions/00000000-0000-0000-0004-000000000001')
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0006-000000000001":["00000000-0000-0000-0005-000000000001","00000000-0000-0000-0001-000000000001","00000000-0000-0000-0004-000000000001","description"]}\n'
            )

    def test_register(self):
        with app.test_client() as client:
            post_data = {'email': 'test_user@example.com', 'password': 'test_user'}
            result = client.post('/register', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_auth(self):
        with app.test_client() as client:
            post_data = {'email': 'student1@example.com', 'password': 'student1'}
            result = client.post('/auth', data = post_data)
            self.assertEqual(
                result.data,
                b'OK'
            )

    def test_post_profile(self):
        with app.test_client() as client:
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
