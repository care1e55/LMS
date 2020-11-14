from . import Base
from . import Column, String, Integer

class Admins(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True)
    user_id = Column(String)