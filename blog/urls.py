"""
This file is used to map the app to the urls
"""
from django.urls import path
# Import views.py file (. means the current directory)
from . import views
# Import class based view
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    # Home page view | views.home : the function in the view | name : the name of route
    # Change views.home to PostListView to use the class based view
    path('', PostListView.as_view(), name = 'blog-home'),
    # User post list view
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    # Detail view (the url contains variable : blog 1 = post/1/, blog 2 = post/2/)
    # pk : primary key -> since this variable is integer then we can specify the type
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), 
    # Create view
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),   
    # Update view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'), 
    # Delete view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'), 
    # About us page view
    path('about/', views.about, name = 'blog-about'),
]

