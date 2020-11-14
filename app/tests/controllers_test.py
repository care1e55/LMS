import json
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
            connection.execute(text(open(cls.initdb_path).read()))
            connection.execute(text(open(cls.test_data_path).read()))
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
                b'{"00000000-0000-0000-0000-000000000001":["student1_first_name","student1_middle_name","student1_last_name","student1@example.com","+7-900-111-22-33","Moscow","","vk.com/exmaple","facebook.com/exmaple","instagram.com/exmaple","day","free"]}\n'
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


    