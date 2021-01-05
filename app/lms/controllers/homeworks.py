from . import *

# add new homework to course
@app.route('/homework', methods = ['POST'])
def post_homework():
    session = Session()
    session.add(Homeworks(**request.form))
    session.commit()
    return 'OK', 200
    session.close()

# change or delete homework
# TODO: same
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
