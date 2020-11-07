from . import Base
from . import Column, String, Integer

class Courser(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    description = Column(String)

    # def __repr__(self):
    #     return f'txt={self.txt}, num={self.num}'