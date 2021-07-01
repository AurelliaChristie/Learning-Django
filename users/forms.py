from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Import Profile model
from .models import Profile

# Register Form
class UserRegisterForm(UserCreationForm):
    # If it is not required just type in required = False
    email = forms.EmailField()

    # Save the data from the form into the fields in User model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Update User Form (can't reset password in this case)
# ModelForm : create a form that would work with specific database Models (in this case it is User Models)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Save the data from the form into the fields in User model
    class Meta:
        model = User
        fields = ['username', 'email']

# Update Profile Form (update picture profile)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
