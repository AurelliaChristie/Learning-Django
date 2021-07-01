from django.db import models
# To add datetime
from django.utils import timezone
# Import user models (later on will be used in one to many relationship)
from django.contrib.auth.models import User
# Import reverse function
from django.urls import reverse

# Create table
class Post(models.Model):
    # Fields in the table 
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now : update the date_posted to the current date time everytime the post is updated
    # auto_now_add : update the date_posted to the current date time when the post is added
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete : what the app should do when the author of a post is deleted frome the user base
    # models.CASCADE : delete the post when the author is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Save the Post object with the title as the key
    def __str__(self):
        return self.title

    # Redirect link after a new post is created
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

