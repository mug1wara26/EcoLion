import bcrypt
import sys
import os
import jwt
import bcrypt
from config import dbfetch, app, dbcommit

class User:
    def __init__(self, user_id=None, name=None, email=None, bio=None, hash=None, lat=None, lng=None, car_capacity=None):
        self.id = user_id
        self.name = name
        self.email = email
        self.bio = bio
        self.hash = hash
        self.lat = lat
        self.lng = lng
        self.car_capacity = car_capacity


def get_user_by_id(user_id):
    user_dict =  dbfetch("SELECT * FROM User WHERE id=%s", (user_id,), one=True)
    return User(
            user_dict['id'],
            user_dict['name'],
            user_dict['email'],
            user_dict['biography'],
            user_dict['password_hash'],
            user_dict['latitude'],
            user_dict['longitude']
            )

def login_with_token(token):
        decoded_data = jwt.decode(jwt=token,
                                  key=app.secret_key,
                                  algorithms=["HS256"])
        return get_user_by_id(decoded_data['user_id'])

def generate_jwt(user_id, username):
    return jwt.encode({"user_id": user_id, "username": username}, app.secret_key, algorithm="HS256")

def register(user_data):  # token
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']
    phone_number = user_data['number']
    lat = user_data['lat']
    lng = user_data['lng']
    capacity = user_data['car_capacity']

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    query = "INSERT INTO User (name, email, password_hash, phone_number, latitude, longitude, car_capacity) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dbcommit(query, (username, email, hash, phone_number, lat, lng, capacity))
    query = "SELECT id FROM User WHERE email=%s"
    user_id = dbfetch(query, (email,))[0]['id']

    return generate_jwt(user_id, username)

def login(user_data):
    email = user_data['email']
    password = user_data['password']
    bytes = password.encode('utf-8')

    # Get user_id,username and hash from database using email
    user_id = 1
    username = 'test'
    hash = b'$2b$12$b0jQ7Gmhc.tlvHWLHpb4Re.0WNI8.tUU3bbzJYhAqE3Z.lGMZcsRK'
    if bcrypt.hashpw(bytes, hash) == hash:
        return generate_jwt(user_id, username)
    else:
        return None

def edit_user(user_id: int, user: User):
    pass

def delete_user(user_id: int):
    pass
