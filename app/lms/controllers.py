from lms import app
from sqlalchemy import create_engine
import json

db_string = "postgresql://postgres:example@localhost:5432/postgres"
db = create_engine(db_string)

@app.route('/')
def hello_world():
    result_set = db.execute("SELECT num_col, text_col FROM TEST")
    result = {}
    for r in result_set:  
        result[r[0]] = r[1]
    return json.dumps(result)





