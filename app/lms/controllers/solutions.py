from flask import Blueprint, request, redirect, url_for, g
from lms.model.solutions import Solutions
from lms.model.auth import Auth 
import logging

from . import Session

solution_api = Blueprint('solution_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@solution_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    email = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(email=email).first()
    session.close()
    if g.user is None:
        redirect(url_for('/')) 

# TODO: homework task support
# TODO: add check pass date support
@solution_api.route('/solution', methods = ['POST'])
def post_solution():
    logger.log(logging.INFO, request.form)
    session = Session()
    session.add(Solutions(**request.form))
    session.commit()
    session.close()
    return 'OK', 200

# view homeworks solutions
# TODO: add check if student on course support
@solution_api.route('/solutions/<course_id>', methods = ['GET'])
def solutions(course_id):
    session = Session()
    result_set = session.query(Solutions) \
        .filter(Solutions.course_id == course_id) \
        .all()
    result = {}
    for solutions in result_set:
        result[str(solutions.solution_id)] = [
            solutions.homework_id,
            solutions.student_id,
            solutions.course_id,
            solutions.description
        ]
    session.close()
    logger.log(logging.INFO, result)
    return result, 200
