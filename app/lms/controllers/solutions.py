from . import *
from .. import app

# TODO: homework task support
# TODO: add check pass date support
@app.route('/solution', methods = ['POST'])
def post_solution():
    session = Session()
    session.add(Solutions(**request.form))
    session.commit()
    return 'OK', 200
    session.close()

# view homeworks solutions
# TODO: add check if student on course support
@app.route('/solutions/<course_id>', methods = ['GET'])
def solutions(course_id):
    session = Session()
    result_set = session.query(Solutions) \
        .filter(Solutions.course_id == course_id) \
        .all()
    result = {}
    for solutions in result_set:
        result[str(solutions.solution_id)] = [
            solutions.homework_id,
            solutions.student_id,
            solutions.course_id,
            solutions.description
        ]
    session.close()
    return result, 200