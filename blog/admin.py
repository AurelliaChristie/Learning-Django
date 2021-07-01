from django.contrib import admin

# Import model
from .models import Post

# To add our model to the admin page
admin.site.register(Post)
