from flask import Blueprint, request, make_response, g, jsonify,redirect, url_for
from flask_httpauth import HTTPBasicAuth, HTTPDigestAuth
from lms.model.auth import Auth 
import logging

from . import Session

auth_api = Blueprint('auth_api', __name__)
auth_get = Blueprint('auth_get', __name__)
auth_password = HTTPBasicAuth()
auth_token = HTTPDigestAuth()

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
@auth_token.login_required
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
    logger.log(logging.INFO, request.form)
    session = Session()
    user_creds = session.query(Auth).filter(
        Auth.registration_code == request.form['registration_code']) 
    if session.query(user_creds.exists()).scalar():
        session.query(Auth) \
            .filter(Auth.user_id == str(user_creds.all()[0].user_id)) \
            .update({"is_active" : True})
        session.commit()
    session.close()
    return 'OK', 200

@auth_api.route('/test', methods = ['GET'])
def test():
    response = make_response(str(g.token))
    return response

@auth_password.verify_password
def verify_password(user_id, password):
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    if g.user is None:
        return False
    return g.user.verify_password(password)

# @auth_token.verify_password
# def verify_auth_token(token, unused):

#     g.user = Auth.verify_auth_token(token)
#     return g.user is not None

@auth_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    session.close()
    if g.user is None:
        redirect(url_for('/')) 

@auth_password.error_handler
def unauthorized():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please authenticate'})
    response.status_code = 401
    return response

# authentication token route
@auth_get.route('/get-auth-token')
@auth_password.login_required
def get_auth_token():
    response = make_response(jsonify({'token': g.user.generate_auth_token()}))
    response.set_cookie('token', g.user.generate_auth_token())
    return response, 200
