from sqlalchemy import create_engine
from sqlalchemy import func, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from lms.model import *
import json
import os

host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
password = os.environ['POSTGRES_PASSWORD']
schema = os.environ['POSTGRES_SCHEMA']

db_string = f'postgresql://{schema}:{password}@{host}:{port}/{schema}'
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)
