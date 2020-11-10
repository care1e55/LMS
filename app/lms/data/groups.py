from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'courses'

    group_id = Column(String, primary_key=True, default = uuid.uuid4)
    group_name = Column(String)
    faculty_name = Column(String)
    course_num = Column(String)