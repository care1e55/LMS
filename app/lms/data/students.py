from . import Base
from . import Column, String, Integer

class Users(Base):
    __tablename__ = 'users'

    student_id = Column(String, primary_key=True)
    user = Column(String)
    phone_number = Column(String)
    city = Column(String)
    about = Column(String)
    vk_link = Column(String)
    facebook_link = Column(String)
    linkedin_link = Column(String)
    instagram_link = Column(String)