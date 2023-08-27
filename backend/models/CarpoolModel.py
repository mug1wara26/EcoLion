import sys
import os
from config import dbfetch, dbcommit
from UserModel import User

class Carpool():
    CARPOOL_EVENT_TYPE = 'P'
    def __init__(self, carpool_id, name, description, community_id, date):
        self.carpool_id = carpool_id
        self.name = name
        self.description = description
        self.community_id = community_id
        self.date = date

def get_contacts(user_id):
    pass

def create_carpool(description, community_id, date, latitude, longitude, type):
    # creates a carpool that is linked to an organization
    query = "INSERT INTO Event (description, community_id, date, latitude, longitude, type) VALUES (%s,%s,%s,%s,%s,%s)"
    dbcommit(query, (description, community_id, date, latitude, longitude, type))
    return None

def get_carpool_users(carpool_id):
    # returns a list of User objects for the current carpool event
    query = """SELECT u.id, u.name, u.latitude, u.longitude, u.car_capacity, u.phone_number FROM User u, Participating p, Event e
               WHERE p.user_id = u.id and p.event_id = %s and p.event_id = e.id and e.type = %s"""
    data = dbfetch(query, (carpool_id, Carpool.CARPOOL_EVENT_TYPE))
    return list(data)

def log_points(user_id, carpool_id, num_points):
    query = """UPDATE Joined j, Event e SET j.points = j.points + %s WHERE j.user_id = %s and e.id = %s and j.community_id = e.community_id"""
    dbcommit(query, (num_points, user_id, carpool_id))

def join_carpool(user_id, carpool_id):
    pass

def leave_carpool(user_id, carpool_id):
    pass

def update_cluster_number(carpool_id):
    # get users going to the event from the database

    # use kmean algo

    # updates database of ppl going to event by cluster: <user_id>, <cluster_number>

    pass # returns name, id, location, label (clustering identification), car_capacity/owns a car

def kmean_algo(participants):
    pass

def get_carpool_by_userid(carpool_id, user_id):
    #return people who are in the same journey as op
    pass
