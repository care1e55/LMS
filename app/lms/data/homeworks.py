from . import Base
from . import Column, String, Integer

class Homeworks(Base):
    __tablename__ = 'homeworks'

    homework_id = Column(Integer, primary_key=True)
    homeworks_name = Column(String)
    homework_start_date = Column(String)
    homework_end_date = Column(String)
    description = Column(String)
    course_id = Column(String)
