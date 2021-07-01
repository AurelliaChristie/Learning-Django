# To use our templates | to get the 404 page if there is no object
from django.shortcuts import render, get_object_or_404
# Import the Post models (. : current directory)
from .models import Post
# Import class based view
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
# Import Mixins (log in required before we use certain feature)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
# Import User model
from django.contrib.auth.models import User

# Dummy data (replaced by Post models)
# posts = [
#     {
#         'author': 'AurelC',
#         'title':'Blog Post 1',
#         'content': 'First post content',
#         'date_posted':'June 15, 2021'
#     },
#     {
#         'author': 'CoreyMS',
#         'title':'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted':'June 16, 2021'
#     }
# ]

# Create function to open up home page 
def home(request):
    context = {
        # key : our data
        # Before change it into the Post models 'posts': posts
        'posts' : Post.objects.all()
    }
    # (input, subdirectory of the template, data) 
    # In the background there is HttpResponse(...)
    return render(request, 'blog/home.html', context)

# List View : to see the list of the post
class PostListView(ListView):
    model = Post
    # Change the template name from Post_list.html to home.html
    template_name = 'blog/home.html'
    # Change the variable name (the original : objectlist)
    context_object_name = 'posts'
    # Order the post from the latest post to the oldest post
    ordering = ['-date_posted']
    # Create pages in our web (5 post in 1 page)
    paginate_by = 5

# User Post List View : to see the list of the post a user created
class UserPostListView(ListView):
    model = Post
    # Change the template name from Post_list.html to user_posts.html
    template_name = 'blog/user_posts.html'
    # Change the variable name (the original : objectlist)
    context_object_name = 'posts'
    # Create pages in our web (5 post in 1 page)
    paginate_by = 5

    # Overwrite this method to change the query (so that we can filter the post according to the clicked author) 
    def get_queryset(self):
        # Get the user associated with the username we got from the url
        # If the user exists save it to user variable if not return 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # Return the filtered list
        return Post.objects.filter(author = user).order_by('-date_posted')

# Detail View : to see the detail of the post (remember: template will be blog/Post_detail.html)
class PostDetailView(DetailView):
    model = Post

# Create View : to create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Create the author of the post
    def form_valid(self, form):
        # Set the author
        form.instance.author = self.request.user
        # Run form_valid method from the parent class
        return super().form_valid(form)

# Update View : to update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Create the author of the post
    def form_valid(self, form):
        # Set the author
        form.instance.author = self.request.user
        # Run form_valid method from the parent class
        return super().form_valid(form)

    # UserPassesTestMixin
    def test_func(self):
        # Get the exact post that we currently updated
        post = self.get_object()
        # Check if the current log in user is the author of the post
        if self.request.user == post.author:
            return True
        return False

# Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # Success url : if they finish delete the post
    success_url = '/'

    # UserPassesTestMixin
    def test_func(self):
        # Get the exact post that we currently updated
        post = self.get_object()
        # Check if the current log in user is the author of the post
        if self.request.user == post.author:
            return True
        return False

# Create function to open up about us page
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})