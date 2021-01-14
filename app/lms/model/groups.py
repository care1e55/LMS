from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'courses'

    group_id = Column(String, primary_key=True)
    group_name = Column(String)
    faculty_name = Column(String)
    course_num = Column(String)
