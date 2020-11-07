from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Testtable(Base):
    __tablename__ = 'test_table'

    txt = Column(String)
    num = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'txt={self.txt}, num={self.num}'


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
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
            id={self.user_id}, 
            first_name={self.first_name},
            middle_name = 
            last_name = 
            user_role = 
            email = 
            phone_number = 
            city = 
            about = 
            vk_link = 
            facebook_link = 
            linkedin_link = 
            instagram_link = 
            '''