from django.db import models
# Import user model
from django.contrib.auth.models import User
# Import pillow library
from PIL import Image

# Create Profile model
class Profile(models.Model):
    # Create one to one relationship between our user and User models
    # CASCADE : if the user is deleted, the profile will also be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Create image field
    image = models.ImageField(default = "default.jpg", upload_to = 'profile_pics')

    # How we want to print the profile (without this one, the output will only be profile object)
    def __str__(self):
        return f'{self.user.username} Profile'

    # Save image with smaller size (this is a function that has been already exist in our parent class -> run when the model is saved)
    def save(self):
        # Save method of our parent class : super() -> parent class
        super().save()

        # Grab the image & resize it
        # Open the image of the current instance
        img = Image.open(self.image.path)
        
        # Check the image size
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            # Resize the image
            img.thumbnail(output_size)
            # Overwrite the image
            img.save(self.image.path)