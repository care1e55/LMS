from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    student_id = Column(String, primary_key=True, default=uuid.uuid4)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    group_id = Column(String)
    enter_year = Column(String)
    major = Column(String)
    education_form = Column(String)
    education_base = Column(String)
    user_id = Column(String)

    def __repr__(self):
        return f'''student_id={self.student_id}, 
            first_name={self.first_name}, 
            middle_name={self.middle_name}, 
            last_name={self.last_name},
            group_id={self.group_id},
            enter_year={self.enter_year},
            major={self.major},
            education_form={self.education_form},
            education_base={self.education_base},
            user_id={self.user_id}'''  
  