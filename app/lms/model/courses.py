from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(String, primary_key=True, default = uuid.uuid4)
    course_name = Column(String)
    description = Column(String)
    group_id = Column(String)
    teacher_id = Column(String)
    major_id = Column(String)
    