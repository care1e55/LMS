from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Solutions(Base):
    __tablename__ = 'solutions'

    solution_id = Column(String, primary_key=True, default = uuid.uuid4)
    homework_id = Column(String)
    student_id = Column(String)
    course_id = Column(String)
    description = Column(String)
