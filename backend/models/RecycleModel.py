import sys
import os
from config import dbfetch, dbcommit

class Post:
    def __init__(self, post_id=None, title=None, content=None, img_url=None, date=None, author_id=None, community_id=None, status=None, post_type=None):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.img_url = img_url
        self.date = date
        self.author_id = author_id
        self.community_id = community_id
        self.status = status
        self.post_type = post_type

def create_recycle(user_id, post):
    query = "INSERT INTO Post (title, content, resource_url, GET_DATE(), author_id, community_id, status, type) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dbcommit(query, (post.title, 
                     post.content, 
                     post.resource_url,
                     user_id, 
                     post.community_id, 
                     post.status, 
                     post.post_type))
    
def get_recycle_posts_from_user_id():
    pass
    
def get_recycle_posts_from_community(community_id):
    query = """SELECT title, content, resource_url, date, author_id, status, type FROM Post WHERE community_id = %s"""
    data = dbfetch(query, (community_id,))
    return data

def accept_recycle(user_id, recycle_id):
    pass

def get_recycle(recycle_id):
    pass

def is_user_creator(user_id, recycle_id):
    pass

def edit_recycle(user_id, recycle):
    pass

def delete_recycle(user_id, recycle_id):
    pass

def undo_recycle(user_id, recycle_id):
    pass