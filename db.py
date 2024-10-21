from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import *

from pathlib import Path

Path("database") \
    .mkdir(exist_ok=True)
    
engine = create_engine("sqlite:///database/main.db", echo = False)

Base.metadata.create_all(engine)

def insert_user(username, password, role):
     with Session(engine) as session:
        user = User(username = username, password = password, role = role)
        session.add(user)
        session.commit()   

def get_user(username):
     with Session(engine) as session:
         return session.query(User).filter(User.username == username).first()    
     
def attempt_login(username, password):
     with Session(engine) as session:
        query = session.query(User)
         
        if username:
             query = query.filter(User.username == username)
             
        if password:
             query = query.filter(User.password == password)
            
        return query.all()

def insert_package(title, category, content, price, duration, image):
    with Session(engine) as session:
        package = Package(title = title, content = content,
                          category = category, price = price, duration = duration,
                          image = image)
        session.add(package)
        session.commit()
        
def get_packages(categories, min_price, max_price, durations):
    with Session(engine) as session:
        query = session.query(Package)
        
        if categories:
            query = query.filter(Package.content.in_(categories))
            
        if min_price is not None:
            query = query.filter(Package.price >= min_price)

        if max_price is not None:
            query = query.filter(Package.price <= max_price)

        if durations:
            query = query.filter(Package.duration.in_(durations))
            
        return query.all()
    
def delete_package(id):
    with Session(engine) as session:
        package = session.query(Package).filter(Package.id == id).first()
        if package:
            session.delete(package)
            session.commit()
        else:
            raise ValueError("No item found")
 
def update_package(id, title, content, category, price, duration, image):
    with Session(engine) as session:
        package = session.query(Package).filter(Package.id == id).first()
        if package:
            package.title = title
            package.content = content
            package.category = category
            package.price = price
            package.duration = duration
            package.image = image
            session.commit()
        else:
            raise ValueError("No item found")

def get_package_by_id(id):
    with Session(engine) as session:
        if id:
            return session.query(Package).filter(Package.id == id).first()
        
            

