from . import Base
from . import Column, String, Integer

class Teachers(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    phone_number  = Column(Integer)
    city = Column(Integer)
    about = Column(Integer)
    course_id = Column(String)
