#!/usr/bin/env python

'''
Created on Aug 26, 2013

@author: lior
'''

from django.contrib.auth.signals import user_logged_in
from social_auth.models import UserSocialAuth
import facebook

def do_stuff(sender, user, request, **kwargs):
    
    instance = UserSocialAuth.objects.filter(provider='facebook').get()
    oauth_access_token = instance.tokens['access_token']
    graph = facebook.GraphAPI(oauth_access_token)
    profile = graph.get_object("me")
    friends = graph.get_connections("me", "friends")
    

user_logged_in.connect(do_stuff)
