from django.shortcuts import render_to_response
from django.template import RequestContext

from crowdsourcing.models import Survey

from django.contrib.auth.signals import user_logged_in
from social_auth.models import UserSocialAuth
import facebook
import json, os
from django.conf import settings
from django.http import HttpResponseRedirect

def home(request):
    latest_survey = None
    surveys = Survey.live.order_by('-survey_date')
    if surveys:
        latest_survey = surveys[0]
    return render_to_response(
        "home.html",
        {"latest_survey": latest_survey},
        RequestContext(request))


def newUserScript(request):

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
        
    redirectUrl = request.GET.get('next')
    
    return HttpResponseRedirect(redirectUrl)
    
    