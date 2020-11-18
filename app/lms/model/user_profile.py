from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profile'

    profile_id = Column(String, primary_key=True, default=uuid.uuid4)
    user_id = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    about = Column(String)
    vk_link = Column(String)
    facebook_link = Column(String)
    linkedin_link = Column(String)
    instagram_link = Column(String)


    def __repr__(self):
        return f'''
            profile_id={self.profile_id}, 
            user_id={self.user_id}, 
            email={self.email}, 
            phone_number={self.phone_number},
            city={self.city},
            about={self.about},
            vk_link={self.vk_link},
            facebook_link={self.facebook_link},
            linkedin_link={self.linkedin_link},
            instagram_link={self.instagram_link}
            '''


