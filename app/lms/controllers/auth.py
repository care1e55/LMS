from flask import Blueprint, request, make_response
from lms.model.auth import Auth 
import logging

from . import Session

auth_api = Blueprint('auth_api', __name__)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

# auth as admin, teacher or student
# TODO: add roles model
# TODO: add cookie with session id, and session tables
@auth_api.route('/auth', methods = ['POST'])
def auth():
    session = Session()
    user_creds = session.query(Auth).filter(
        Auth.email == request.form['email'], 
        Auth.password == request.form['password'])
    if session.query(user_creds.exists()).scalar():
        response = make_response("OK")
        response.set_cookie('current_user_id', str(user_creds.all()[0].user_id))
        session.close()
        logger.log(logging.INFO, response)
        return response, 200
    else:
        session.close()
        return 'Bad credentials', 400

@auth_api.route('/password/<user_id>', methods = ['POST'])
def change_password(user_id):
    session = Session()
    user_creds = session.query(Auth) \
        .filter(Auth.user_id == user_id) \
        .update({"password" : request.form['password']})
    session.commit()
    session.close()
    logger.log(logging.INFO, user_creds)
    return 'OK', 200

# register new user
# TODO: add registration code support
@auth_api.route('/register', methods = ['POST'])
def register():
    session = Session()
    session.add(
        Auth(email = request.form['email'], 
        password = request.form['password']))
    session.commit()
    session.close()
    logger.log(logging.INFO, '{} {}', request.form['email'], request.form['password'])
    return 'OK', 200
