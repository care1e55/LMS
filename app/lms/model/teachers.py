from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Teachers(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(String, primary_key=True, default=uuid.uuid4)
    user_id = Column(String)
    phone_number  = Column(String)
    city = Column(String)
    about = Column(String)
    course_id = Column(String)
