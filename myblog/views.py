from django.shortcuts import render, get_object_or_404
import requests
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PostListView(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'myblog/account.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	
class PostDetailView(LoginRequiredMixin,DetailView):
	model = Post
	
class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/user/accounts'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
