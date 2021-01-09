from flask import Blueprint
from lms.model.students import Students
import logging

from . import Session

groups_api = Blueprint('groups_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

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
