from lms import app
from flask import request
from sqlalchemy import create_engine
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
