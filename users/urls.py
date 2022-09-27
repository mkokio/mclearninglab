"""Define URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
        #These default URLs include named URL patterns, such as 'login' and
        #'logout'. We set the variable app_name to 'users' so Django can distinguish
        #these URLs from URLs belonging to other apps
        #Even default URLs provided by Django, when included in the users app’s
        #urls.py file, will be accessible through the users namespace.
urlpatterns = [
    #Include default auth urls
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')  #registration page
]
#(above)When Django reads this URL, the word users tells Django to look in
#users/urls.py, and login tells it to send requests to Django’s default login view
