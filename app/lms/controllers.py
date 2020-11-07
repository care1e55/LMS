from lms import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lms.data import *
import json

db_string = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

# @app.route('/')
# def hello_world():
#     result_set = db.execute("SELECT num_col, text_col FROM TEST")
#     result = {}
#     for r in result_set:  
#         result[r[0]] = r[1]
#     return json.dumps(result)


@app.route('/users')
def users():
    session = Session()
    rows = session.query(Users).all()
    res = [rw for rw in rows]
    print(res)
    session.close()
    return res

# POST
@app.route('/auth')
def auth():
    pass

# POST
@app.route('/register')
def register():
    pass

# GET
@app.route('/profile')
def profile():
    pass

# POST
@app.route('/profile')
def profile():
    pass

# GET
@app.route('/groups')
def groups():
    pass

# GET
@app.route('/courses')
def courses():
    pass

# GET
@app.route('/course')
def course():
    pass

# POST
@app.route('/course')
def course():
    pass

# POST
@app.route('/homework')
def homework():
    pass

# GET
@app.route('/homework')
def homework():
    pass
