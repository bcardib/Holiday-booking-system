from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Package(Base):
    __tablename__ = 'Package'
    id = Column(Integer, primary_key = True)
    title = Column(String)
    content = Column(String)
    category = Column(String)
    price = Column(Integer)
    duration = Column(String)
    image = Column(String)
    
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)  
    role = Column(String)
