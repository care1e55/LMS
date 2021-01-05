from . import *

# view user courses
# TODO: teacher/student courses diference
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

# view course info
# TODO: and major (староста) support 
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
