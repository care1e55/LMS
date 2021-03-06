from flask import Blueprint, request, redirect, url_for, g, make_response
from lms.model.user_profile import UserProfile
from lms.model.students import Students 
from lms.model.auth import Auth
import logging

from . import Session

profile_api = Blueprint('profile_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@profile_api.before_request
def before_request():
    print("BEFORE REQUEST")
    g.token = request.cookies.get('token')
    email = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(email=email).first()
    session.close()
    if g.user is None:
        redirect(url_for('/')) 

# profile change
# TODO: add education base visibility support
# TODO: PUT
@profile_api.route('/profile/<user_id>', methods = ['GET', 'POST', 'PUT'])
def profile(user_id):
    logger.log(logging.INFO, request.form)
    session = Session()
    if request.method == 'GET':
        result_set = session.query(UserProfile, Students, Auth) \
            .filter(UserProfile.user_id == user_id) \
            .join(Students, UserProfile.user_id == Students.user_id) \
            .join(Auth, UserProfile.user_id == Auth.user_id) \
            .all()
        result = {}
        for user_profile, students, auth in result_set:
            result[str(auth.user_id)] = [
                students.first_name,
                students.middle_name,
                students.last_name,
                user_profile.email,
                user_profile.phone_number,
                user_profile.city,
                user_profile.about,
                user_profile.vk_link,
                user_profile.facebook_link,
                user_profile.instagram_link,
                students.education_form
            ]
        session.close()
        logger.log(logging.INFO, result)
        return result, 200
    elif request.method == 'POST':
        session.add(UserProfile(
            **request.form,
            user_id = g.user.user_id
            ).validate())
        session.commit()
        session.close()
        return 'OK', 200

# view self profile
@profile_api.route('/profile', methods = ['GET'])
def self_profile():
    logger.log(logging.INFO, str(g.user.user_id))
    return redirect(f'/profile/{str(g.user.user_id)}')

# cahnge password
@profile_api.route('/password', methods = ['POST'])
def change_password():
    session = Session()
    user_creds = session.query(Auth) \
        .filter(Auth.email == request.form['email']) \
        .update({"password" : request.form['password']})
    session.commit()
    session.close()
    logger.log(logging.INFO, user_creds)
    return 'OK', 200
