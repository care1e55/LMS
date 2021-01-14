from flask import Blueprint, request, redirect, url_for, g
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
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
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
        # TODO: fix
        # print(result_set)
        # if request.cookies.get('current_user_id') == str(result_set['auth'].user_id):
        #     for user_profile, students, auth in result_set:
        #         result[str(auth.user_id)] = [
        #             students.first_name,
        #             students.middle_name,
        #             students.last_name,
        #             user_profile.email,
        #             user_profile.phone_number,
        #             user_profile.city,
        #             user_profile.about,
        #             user_profile.vk_link,
        #             user_profile.facebook_link,
        #             user_profile.instagram_link,
        #             students.education_form,
        #             students.education_base,
        #         ]
        # else:
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
            user_id = user_id
            ).validate())
        session.commit()
        session.close()
        return 'OK', 200

# TODO: fix
# # view self profile
# @profile_api.route('/profile', methods = ['GET', 'POST', 'PUT'])
# def profile(user_id):
#     cur_user_id = request.cookies.get('cur_user_id')
#     return make_response(redirect(f"/profile/<{cur_user_id}>")), 200
