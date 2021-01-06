from flask import Blueprint, request, make_response, render_template, url_for, redirect
from lms.model import Solutions
import json

from . import Session

solution_api = Blueprint('solution_api', __name__)

# TODO: homework task support
# TODO: add check pass date support
@solution_api.route('/solution', methods = ['POST'])
def post_solution():
    session = Session()
    session.add(Solutions(**request.form))
    session.commit()
    return 'OK', 200
    session.close()

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
    return result, 200