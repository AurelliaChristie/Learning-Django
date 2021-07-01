# Import post_save : signal that gets fired after an object is saved (after a user is created)
from django.db.models.signals import post_save
# Import user model -> the sender of the signal
from django.contrib.auth.models import User
# Import the receiver -> receive the signal & perform some task
from django.dispatch import receiver
# Import profile from our models
from .models import Profile

# We want a user profile to be created for each new user
@receiver(post_save, sender = User) # If the user is saved, send the signal 
# kwargs : accept any additional keywords argument
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User) # If the user is saved, send the signal 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()