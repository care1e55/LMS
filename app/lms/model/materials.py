from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Materials(Base):
    __tablename__ = 'materials'

    material_id = Column(String, primary_key=True, default = uuid.uuid4)
    material_name = Column(String)
    material_content = Column(String)
    add_date = Column(String)
    course_id = Column(String)

    