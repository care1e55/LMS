from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Homeworks(Base):
    __tablename__ = 'homeworks'

    homework_id = Column(String, primary_key=True, default = uuid.uuid4)
    homeworks_name = Column(String)
    homework_start_date = Column(String)
    homework_end_date = Column(String)
    description = Column(String)
    course_id = Column(String)
