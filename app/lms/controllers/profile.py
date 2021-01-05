from . import *
from .. import app

# profile change
# TODO: add education base visibility support
# TODO: PUT
@app.route('/profile/<user_id>', methods = ['GET', 'POST', 'PUT'])
def profile(user_id):
    session = Session()
    if request.method == 'GET':
        result_set = session.query(UserProfile, Students, Auth) \
            .filter(UserProfile.user_id == user_id) \
            .join(Students, UserProfile.user_id == Students.user_id) \
            .join(Auth, UserProfile.user_id == Auth.user_id) \
            .all()
        result = {}
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
        return result, 200
    elif request.method == 'POST':
        session.add(UserProfile(
            **request.form,
            user_id = user_id
            ).validate())
        session.commit()
        return 'OK', 200
    session.close()


# # view self profile
# @app.route('/profile', methods = ['GET', 'POST', 'PUT'])
# def profile(user_id):
#     cur_user_id = request.cookies.get('cur_user_id')
#     return make_response(redirect(f"/profile/<{cur_user_id}>")), 200
