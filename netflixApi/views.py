from django.shortcuts import render
import requests,json
import os
import environ
from decouple import config,Csv
from googleapiclient.discovery import build

# Create your views here.
def home1(request,category):
    # url = env("TRENDING")
    # print (url)
    # url = 'https://api.themoviedb.org/3/movie/popular?api_key=4cb8d19a47413735066d0a13e6ced170&language=en-US&page=1'
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

def youtube(request):
    yTubeKey =  config('yTubeKey')
    youtube = build('youtube','v3',developerkey = yTubeKey)
    req = youtube.search(q = 'avengers',part = 'snippet',type= 'video')
    res = req.execute()
    print(res)


