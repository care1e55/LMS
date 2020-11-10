from lms import app
from flask import request
from sqlalchemy import create_engine
from sqlalchemy import func, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from lms.data import *
import json

db_string = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)


@app.route('/auth', methods = ['POST'])
def auth():
    session = Session()
    user_creds = session.query(Auth).filter(
        Auth.email == request.form['email'], 
        Auth.password == request.form['password'])
    if session.query(user_creds.exists()).scalar():
        session.close()
        return 'OK', 200
    else:
        session.close()
        return 'Bad credentials', 400


@app.route('/register', methods = ['POST'])
def register():
    session = Session()
    session.add(Auth(email = request.form['email'], password = request.form['password']))
    session.commit()
    session.close()
    return 'OK', 200


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
        for user_profile, students, auth in result_set:
            result[str(auth.user_id)] = [
                students.first_name,
                students.middle_name,
                students.last_name,
                auth.email,
                user_profile.phone_number,
                user_profile.city,
                user_profile.about,
                user_profile.vk_link,
                user_profile.facebook_link,
                user_profile.instagram_link,
                user_profile.education
            ]
        return result, 200
    elif request.method == 'POST':
        session.add(UserProfile(
            **request.form,
            user_id = user_id
            ))
        session.commit()
        return 'OK', 200
    session.close()


@app.route('/groups/<user_id>', methods = ['GET'])
def groups(user_id):
    session = Session()
    group_id_result = session.query(Students).filter(Students.user_id == user_id).all()[0].group_id
    result_set = session.query(Students).filter(Students.group_id == group_id_result).all()
    result = {}
    for students in result_set:
        result[str(students.user_id)] = [
            students.first_name,
            students.middle_name,
            students.last_name
        ]
    return result, 200






# # POST
# @app.route('/auth')
# def auth():
#     session = Session()
#     rows = session.query(Auth).all()
#     result = {}
#     for rw in rows:
#         result[str(rw.user_id)] = f'{rw.email}, {rw.password}'
#     session.close()
#     return json.dumps(result), 200

# # POST
# @app.route('/register')
# def register():
#     pass

# # GET
# @app.route('/profile')
# def profile():
#     pass

# # POST
# @app.route('/profile')
# def profile():
#     pass

# # GET
# @app.route('/groups')
# def groups():
#     pass

# # GET
# @app.route('/courses')
# def courses():
#     pass

# # GET
# @app.route('/course')
# def course():
#     pass

# # POST
# @app.route('/course')
# def course():
#     pass

# # POST
# @app.route('/homework')
# def homework():
#     pass

# # GET
# @app.route('/homework')
# def homework():
#     pass
