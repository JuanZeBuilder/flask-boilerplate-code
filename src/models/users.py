import datetime
from os import environ
import importlib


app = importlib.import_module(environ.get("STAGE_ENV"))

db = app.db

class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(200), primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    hashed_password = db.Column(db.String(200))
    email = db.Column(db.String(200))
    creation_date = db.Column(db.DateTime())

    def __init__(self, user_id, first_name, last_name, hashed_password, email, creation_date):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.hashed_password = hashed_password
        self.email = email
        self.creation_date = creation_date

    def json(self):
        dto = {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'hashed_password': self.hashed_password,
            'email': self.email,
            'creation_date': self.creation_date,
        }
        return dto 


def get_all_user():
    user_list = Users.query.all()
    
    if user_list:
        return [user.json() for user in user_list]
    
    return []

def get_user_by_user_id(user_id):
    user = Users.query.filter_by(user_id=user_id).first()
    if user:
        return user.json()
    return None

def get_user_by_email(email):
    user = Users.query.filter_by(email=email).first()
    if user:
        return user.json()
    return None

def create_new_user(user_id, first_name, last_name, hashed_password, email, creation_date):

    to_db = {
        'user_id': user_id, 
        'first_name': first_name, 
        'last_name': last_name,
        'hashed_password': hashed_password,
        'email': email,
        'creation_date': creation_date
    }

    new_user = Users(**to_db)
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        print("create_new_user error: " + str(e))
        print(to_db)
        return False

def update_user_details_by_user_id(user_id, first_name, last_name, password, email):
    user = Users.query.filter_by(user_id=user_id).first()
    if user:
        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        user.email = email
        db.session.commit()
        return True
    
    return False

def delete_user_by_user_id(user_id):
    user = Users.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    
    return False