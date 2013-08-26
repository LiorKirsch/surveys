'''
Created on Aug 26, 2013

@author: lior
'''
from django.contrib.auth.signals import user_logged_in
from social_auth.models import UserSocialAuth
import facebook
import json, os
from django.conf import settings


    
      
def do_stuff(sender, user, request, **kwargs):

    instance = UserSocialAuth.objects.filter(provider='facebook').get()
    oauth_access_token = instance.tokens['access_token']
    graph = facebook.GraphAPI(oauth_access_token)
    profile = graph.get_object("me")
    friends = graph.get_connections("me", "friends")
    likes = graph.get_connections("me", "likes")
    
    userData = {'user': profile, 'friends': friends, 'likes':likes}
    dataDir = settings.DATA_DIR
    fileName = '%s.txt' % profile['username'] 
    fileName = os.path.join(dataDir, fileName)
    
    with open(fileName, 'w') as outfile:
        json.dump(userData, outfile)