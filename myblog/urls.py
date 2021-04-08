from django.urls import path
#from django.contrib import admin
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', views.index, name='myblog-index'),
    path('user/accounts',PostListView.as_view(),name='post-list'),
    path('user/post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('user/post/create', PostCreateView.as_view(), name='create-post'),
    path('user/post/<int:pk>/update', PostUpdateView.as_view(), name='update-post'),
    path('user/post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post')
]
