from django.shortcuts import render, get_object_or_404
import requests
from .models import Post
from django.contrib.auth.models import User



def	news_headlines():
	r = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=ff22b7a71bb34dac9df5571c99f7c961')
	rq = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=ff22b7a71bb34dac9df5571c99f7c961')
	jdata = r.json()
	sdata = rq.json()
	return jdata['articles'],sdata['articles']

def index(request):
	posts,post2 = news_headlines()
	context = {'posts':posts, 'post2':post2}
	return render(request, 'myblog/index.html', context)
