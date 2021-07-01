"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
# Import users/views
from users import views as user_views
# Import views -> for log in 
from django.contrib.auth import views as auth_views
# Import settings & static for adding static MEDIA_URL to our url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin view
    path('admin/', admin.site.urls),
    # Register view
    path('register/', user_views.register, name = 'register'),
    # Profile view
    path('profile/', user_views.profile, name = 'profile'),
    # Login & Logout view
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    # Reset password view
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), 
        name = 'password_reset'),
    # Redirect page after password reset
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), 
        name = 'password_reset_done'),
    # Password reset confirmation (in the back end of passwordresetview)
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), 
        name = 'password_reset_confirm'),
    # Password reset complete view
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), 
        name = 'password_reset_complete'),
    # include function will bring the app to blog/urls.py when the user go to the app route
    # After going into include funciton, the app will not see this file again, instead it will see the blog/urls.py
    path('', include('blog.urls')),
]

# If we are in DEBUG mode, we want to add this to our url patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)