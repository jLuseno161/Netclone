from django.shortcuts import render
import requests,json
import os
import environ
from decouple import config,Csv
from googleapiclient.discovery import build
import tmdbsimple as tmdb
import json
from time import mktime
from datetime import datetime, date
from googleapiclient.errors import HttpError

# Create your views here.
def home1(request,category):
    key =  config('API_KEY')  
    url =  config('url') 
    url2 = url.format(category,key)
    urll = requests.get(url2)
    urlll = urll.json()
    return urlll

def home(request):
    popular = home1(request,'popular')
    upcoming = home1(request,'upcoming')
    latest = home1(request,'latest')
    topRated = home1(request,'top_rated')

    return render(request,'home.html',{'popular':popular,"upcoming":upcoming,"latest":latest,"toprated":topRated})

def youtube(request,id):
    yTubeKey =  config('yTubeKey')
    popular = home1(request,'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = yTubeKey)
    req = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = req.execute()
    return render(request,'youtube.html',{'response':res})



