from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

class Teachers(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer)
    phone_number  = Column(Integer)
    city = Column(Integer)
    about = Column(Integer)
    course_id = Column(String)
