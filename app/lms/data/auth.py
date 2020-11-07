from . import Base
from . import Column, String, Integer

class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    description = Column(String)
    materials  = Column(String)