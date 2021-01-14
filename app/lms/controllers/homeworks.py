from flask import Blueprint, request, redirect, url_for, g
from lms.model.homeworks import Homeworks
from lms.model.auth import Auth 
import logging

from . import Session

homework_api = Blueprint('homework_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@homework_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    session.close()
    if g.user is None:
        redirect(url_for('/')) 

# add new homework to course
@homework_api.route('/homework', methods = ['POST'])
def post_homework():
    logger.log(logging.INFO, request.form)
    session = Session()
    session.add(Homeworks(**request.form))
    session.commit()
    return 'OK', 200
    session.close()

# change or delete homework
# TODO: same
@homework_api.route('/homeworks/<homework_id>', methods = ['PUT', 'DELETE'])
def modify_homwork(homework_id):
    logger.log(logging.INFO, request.form)
    session = Session()
    if request.method == 'PUT':
        session.query(Homeworks) \
            .filter(Homeworks.homework_id == homework_id) \
            .update(
                **request.form,
                homework_id = homework_id)
        session.commit()
    elif request.method == 'DELETE':
        session.query(Homeworks) \
            .filter(Homeworks.homework_id == homework_id) \
            .delete()
        session.commit()
    session.close()
    return 'OK', 200
