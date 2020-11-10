from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Auth(Base):
    __tablename__ = 'auth'

    user_id = Column(String, primary_key=True, default=uuid.uuid4)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'user_id={self.user_id}, email={self.email}, password={self.password}'