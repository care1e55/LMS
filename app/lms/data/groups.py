from . import Base
from . import Column, String, Integer

# class Groups(Base):
#     __tablename__ = 'courses'

#     group_id = Column(Integer, primary_key=True)
#     course_id = Column(String)
#     course_name = Column(String)
#     description = Column(String)
#     teacher_id = Column(String)


class Groups(Base):
    __tablename__ = 'courses'

    group_id = Column(String, primary_key=True)
    group_name = Column(String)
    faculty_name = Column(String)
    course_num = Column(String)