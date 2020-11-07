from . import Base
from . import Column, String, Integer

class Groups(Base):
    __tablename__ = 'courses'

    group_id = Column(Integer, primary_key=True)
    course_id = Column(String)
    course_name = Column(String)
    description = Column(String)
    teacher_id = Column(String)