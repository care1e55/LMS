from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Auth(Base):
    __tablename__ = 'auth'

    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'user_id={self.user_id}, email={self.email}, password={self.password}'