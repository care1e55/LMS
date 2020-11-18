from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid
import re

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

    def validate(self):
        self._validate_vk_link(self.vk_link)
        self._validate_facebook_link(self.facebook_link)
        self._validate_instagram_link(self.instagram_link)
        self._validate_phone(self.phone_number)
        return self

    def _validate_phone(self, phone_number):
        if re.match(r"^\+7(.+?)$", phone_number):
            return self
        else:
            raise Exception("phone number format violation")
        
    def _validate_vk_link(self, vk_link):
        if re.match(r"^https://vk.com/(.+?)$", vk_link):
            return self
        else:
            raise Exception("VK link format violation")
        
    def _validate_facebook_link(self, facebook_link):
        if re.match(r"^https://facebook.com/(.+?)$", facebook_link):
            return self
        else:
            raise Exception("facebook link format violation")
    
    def _validate_instagram_link(self, instagram_link):
        if re.match(r"^https://instagram.com/(.+?)$", instagram_link):
            return self
        else:
            raise Exception("instagram link format violation")


