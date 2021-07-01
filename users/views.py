from django.shortcuts import redirect, render
# To add flash message
from django.contrib import messages
# Add the form that have been inherited from UserCreationFrom
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Import log in required decorators (to restrict user to access certain page if they are not logged in)
from django.contrib.auth.decorators import login_required

# Create register view
def register(request):
    # get request: sent when navigate to the page (open the blank form)
    # post request: validate the form data
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Copy the username to be shown in the message
            username = form.cleaned_data.get('username')
            # message.success(request, the message)
            messages.success(request, f'Your account has been created! You are now able to log in')
            # Redirect back to the home page
            return redirect('login')
    else:
        form = UserRegisterForm()
    # render(input, form template, context)
    return render(request, 'users/register.html', {'form': form})

# User profile view that can be accessed after they log in
@login_required
def profile(request):
    # If this is post route -> form is valid -> create the forms
    if request.method == "POST":
        # What would be run if we submit our form
        # Passed in the post data(updated data), but also keep the instance since we have to know what data to be updated
        u_form = UserUpdateForm(request.POST, instance = request.user)
        # We will also receive file data (profile image) -> request.FILES
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, the message)
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
