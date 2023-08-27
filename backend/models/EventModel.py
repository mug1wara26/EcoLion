import datetime
import sys
import os
from datetime import datetime as dt

class Event:
    def __init__(self, event_id, description, community_id, event_time):
        self.id = event_id
        self.description = description
        self.community_id = community_id
        self.time = event_time

def join_event(user_id, event_id):
    return True

dummy_event = Event(1, "super cool sus event", 69, dt.timestamp(datetime.datetime(2023,10,3,8,30)))

def create_event(community_id, event):
    return dummy_event.id

def get_event(event_id):
    pass

def edit_event(event_id, event):
    pass

def delete_event(event_id):
    pass

def leave_event(user_id, event_id):
    pass

#add the user
#run the carpool cluster algorithm
def add_user(user_id, event_id):
    pass

#remove the user
#run the carpool cluster algorithm
#return response 200 if successful
#return 
def remove_user(user_id, event_id):
    pass