import sys
import os
from enum import Enum
from config import dbfetch, dbcommit


class Community:
    # Types of community members
    MEMBER_TYPE = "M"
    ADMIN_TYPE = "A"

    def __init__(self, community_id, name, description, lat, lng, img_url):
        self.id = community_id
        self.name = name
        self.description = description
        self.lat = lat
        self.lng = lng
        self.img_url = img_url

def create_community(user_id, community):
    dbcommit("""
             INSERT INTO Community
             VALUES (%s, %s, %s, %s, %s);
             """, (community.name, community.description, community.lat, community.lng, community.img_url))

def join_community(user_id, community_id):
    pass

def get_community(community_id):
    return Community(
        1,
        'NUS High School',
        'We know all the digits of pi',
        1.3,
        103,
        'https://cataas.com/cat/says/hello%20world!'
        )

def get_communities():
    return [vars(Community(
        1,
        'NUS High School',
        'Sample description',
        1.3,
        103,
        'url'
        ))]

def get_communities(user_id):
    query = """SELECT c.name, c.description, c.resource_url, c.latitude, c.longitude, c.type FROM Community c, Joined j
               WHERE c.id = j.community_id and j.user_id = %s"""
    return dbfetch(query, (user_id,))

def is_user_admin(user_id, community_id):
    pass

def edit_community(community):
    #users input name, description, location
    pass

def delete_community(community_name, community_id):
    pass

def leave_community(user_id, community_id):
    pass

