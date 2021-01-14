from flask import Blueprint, request, redirect, url_for, g
from lms.model.students import Students
from lms.model.auth import Auth 
import logging

from . import Session

groups_api = Blueprint('groups_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@groups_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    if g.user is None:
        redirect(url_for('/')) 

# users in group
# TODO: self group by user_id?
@groups_api.route('/groups/<user_id>', methods = ['GET'])
def groups(user_id):
    session = Session()
    group_id_result = session.query(Students) \
        .filter(Students.user_id == user_id) \
        .all()[0].group_id
    result_set = session.query(Students) \
        .filter(Students.group_id == group_id_result) \
        .all()
    result = {}
    for students in result_set:
        result[str(students.user_id)] = [
            students.first_name,
            students.middle_name,
            students.last_name
        ]
    session.close()
    logger.log(logging.INFO, result)
    return result, 200
