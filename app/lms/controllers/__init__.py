from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os


host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
password = os.environ['POSTGRES_PASSWORD']
schema = os.environ['POSTGRES_SCHEMA']

db_string = f'postgresql://{schema}:{password}@{host}:{port}/{schema}'
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)
