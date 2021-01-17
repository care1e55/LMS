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

# authentication token route
@auth_get.route('/get-auth-token')
@auth_password.login_required
def get_auth_token():
    response = make_response(jsonify({'token': g.user.generate_auth_token()}))
    response.set_cookie('token', g.user.generate_auth_token())
    return response, 200

# register new user
@auth_get.route('/register', methods = ['POST'])
def register():
    logger.log(logging.INFO, request.form)
    session = Session()
    user_creds = session.query(Auth).filter(
        Auth.email == request.form['email']).filter(
            Auth.password == request.form['password']).filter(
                Auth.registration_code == request.form['registration_code']) 
    if session.query(user_creds.exists()).scalar():
        session.query(Auth) \
            .filter(Auth.user_id == str(user_creds.all()[0].user_id)) \
            .update({"is_active" : True})
        session.commit()
        session.close()
        return 'OK', 200
    else:
        session.close()
        return 'Bad credentials', 400

@auth_password.verify_password
def verify_password(email, password):
    session = Session()
    g.user = session.query(Auth).filter_by(email=email).first()
    if g.user is None or not g.user.is_active:
        return False
    return g.user.verify_password(password)

@auth_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    email = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(email=email).first()
    session.close()
    if g.user is None:
        redirect(url_for('/'))

@auth_password.error_handler
def unauthorized():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please authenticate'})
    response.status_code = 401
    return response

# @auth_token.route('/')
# def unauthorized_token():
#     response = jsonify({'status': 401, 'error': 'unauthorized',
#                         'message': 'please authenticate'})
#     response.status_code = 401
#     return response

# @auth_token.verify_password
# def verify_auth_token(token, unused):

#     g.user = Auth.verify_auth_token(token)
#     return g.user is not None
