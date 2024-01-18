from models.users import *
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

def register_user_service(first_name, last_name, password, email):

    # Generate random user_id and check if user id is already in use
    while True:
        user_id = str(uuid.uuid4())
        user = get_user_by_user_id(user_id)
        if not user:
            break
    
    # generate a hash for the password
    hashed_password = generate_password_hash(password)

    print(hashed_password)

    return create_new_user(user_id, first_name, last_name, hashed_password, email, datetime.now())

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if not user:
        return 0
    
    print(check_password_hash(user['hashed_password'], password))

    if not check_password_hash(user['hashed_password'], password):
        return 1
    
    # User authenticated succesfully
    return 2

