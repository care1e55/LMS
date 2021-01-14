from flask import Blueprint, request, redirect, url_for, g
from lms.model.auth import Auth
from lms.model.students import Students
from lms.model.courses import Courses
import logging

from . import Session

courses_api = Blueprint('courses_api', __name__)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@courses_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    if g.user is None:
        redirect(url_for('/')) 


# view user courses
# TODO: teacher/student courses diference
@courses_api.route('/courses/<user_id>', methods = ['GET'])
def courses(user_id):
    session = Session()
    group_id_result = session.query(Students) \
        .filter(Students.user_id == user_id) \
        .all()[0].group_id
    result_set = session.query(Courses) \
        .filter(Courses.group_id == group_id_result) \
        .all()
    result = {}
    for courses in result_set:
        result[str(courses.course_name)] = [
            courses.description
        ]
    session.close()
    logger.log(logging.INFO, result)
    return result, 200

# view course info
# TODO: and major (староста) support 
@courses_api.route('/course/<course_id>', methods = ['GET'])
def course(course_id):
    session = Session()
    result_set = session.query(Courses) \
        .filter(Courses.course_id == course_id) \
        .all()
    result = {}
    for courses in result_set:
        result[str(courses.course_name)] = [
            courses.description,
            courses.teacher_id,
            courses.major_id
        ]
    session.close()
    logger.log(logging.INFO, result)
    return result, 200
