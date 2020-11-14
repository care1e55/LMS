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
                user_profile.email,
                user_profile.phone_number,
                user_profile.city,
                user_profile.about,
                user_profile.vk_link,
                user_profile.facebook_link,
                user_profile.instagram_link,
                students.education_form,
                students.education_base,
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
    return result, 200


@app.route('/courses/<user_id>', methods = ['GET'])
def courses(user_id):
    session = Session()
    group_id_result = session.query(Students) \
        .filter(Students.user_id == user_id) \
        .all()[0].group_id
    result_set = session.query(Courses) \
        .filter(Courses.group_id == group_id_result) \
        .all()
    result = {}
    for courses in result_set:
        result[str(courses.course_name)] = [
            courses.description
        ]
    session.close()
    return result, 200


@app.route('/course/<course_id>', methods = ['GET'])
def course(course_id):
    session = Session()
    result_set = session.query(Courses) \
        .filter(Courses.course_id == course_id) \
        .all()
    result = {}
    for courses in result_set:
        result[str(courses.course_name)] = [
            courses.description,
            courses.teacher_id,
            courses.major_id
        ]
    session.close()
    return result, 200


@app.route('/material', methods = ['POST'])
def post_material():
    session = Session()
    session.add(Materials(
        **request.form))
    session.commit()
    return 'OK', 200
    session.close()


@app.route('/material/<material_id>', methods = ['PUT', 'DELETE'])
def modify_material(material_id):
    session = Session()
    if request.method == 'PUT':
        session.query(Materials) \
            .filter(Materials.material_id == material_id) \
            .update(
                **request.form,
                material_id = material_id)
        session.commit()
    elif request.method == 'DELETE':
        session.query(Materials).filter(Materials.material_id == material_id).delete()
        session.commit()
    return 'OK', 200
    session.close()


@app.route('/homeworks', methods = ['POST'])
def post_homework():
    session = Session()
    session.add(Homeworks(**request.form))
    session.commit()
    return 'OK', 200
    session.close()


@app.route('/homeworks/<homework_id>', methods = ['PUT', 'DELETE'])
def modify_homwork(homework_id):
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
    return 'OK', 200
    session.close()


@app.route('/solution', methods = ['POST'])
def post_solution():
    session = Session()
    session.add(Solutions(**request.form))
    session.commit()
    return 'OK', 200
    session.close()


@app.route('/solutions/<course_id>', methods = ['GET'])
def solutions(course_id):
    session = Session()
    session.add(Solutions(**request.form))
    session.commit()
    return 'OK', 200
    session.close()
