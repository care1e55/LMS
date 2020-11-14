import json
import unittest
from lms import app

app.testing = True


class TestControllers(unittest.TestCase):

    def test_get_profile(self):
        with app.test_client() as client:
            result = client.get('/profile/00000000-0000-0000-0000-000000000001')
            # print(result.data)
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
            # print(result.data)
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description"]}\n'
            )

    def test_get_course_info(self):
        with app.test_client() as client:
            result = client.get('/course/00000000-0000-0000-0004-000000000001')
            # print(result.data)
            self.assertEqual(
                result.data,
                b'{"course_name_1":["description","00000000-0000-0000-0003-000000000004",""]}\n'
            )

    def test_get_solutions(self):
        with app.test_client() as client:
            result = client.get('/solutions/00000000-0000-0000-0004-000000000001')
            # print(result.data)
            self.assertEqual(
                result.data,
                b'{"00000000-0000-0000-0006-000000000001":["00000000-0000-0000-0005-000000000001","00000000-0000-0000-0001-000000000001","00000000-0000-0000-0004-000000000001","description"]}\n'
            )