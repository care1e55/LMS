from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
# from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os

Base = declarative_base()

class Auth(Base):
    __tablename__ = 'auth'

    user_id = Column(String, primary_key=True, default=uuid.uuid4)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    registration_code = Column(String)
    is_active = Column(Boolean)

    def __repr__(self):
        return f'user_id={self.user_id}, email={self.email}, password={self.password}'

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return (self.password == password)
        # return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(os.environ.get('SECRET_KEY', 'default'), expires_in=expires_in)
        return s.dumps({'user_id': str(self.user_id)}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(os.environ.get('SECRET_KEY', 'default'))
        try:
            data = s.loads(token)
        except:
            return None
        return Auth.query.get(data['user_id'])