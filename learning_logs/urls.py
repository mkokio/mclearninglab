"""Defines URL patterns for learning_logs."""   #To make it clear which urls.py we’re working in, add a docstring at the beginning

from django.urls import path                    #needed when mapping URLs to view
from . import views                             #the dot tells Python to import the views.py module from the same directory as the current urls.py module

app_name = 'learning_logs'                      #variable app_name helps Django distinguish this urls.py file from files of the same name in other apps within the project
urlpatterns = [                                 #variable urlpatterns in this module is a list of individual pages that can be requested from the learning_logs app 
    # Home page
    path('',views.index,name="index"), 
    
    # Page that shows all topics                 #actual url pattern with 3 arguments.
    path('topics/',views.topics, name='topics'),
                                                #1. string that helps Django route the current request properly'
                                                #2. specifies which function to call in views.py
                                                #3. provides the name index for this URL pattern so we can refer to it in other code sections.
                                                # Whenever we want to provide a link to the home page, we’ll use this name instead of writing out a URL
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #path('route the request properly','which function to call in views.py','provides name index in order to use in other code sections')

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/',views.new_entry , name='new_entry'),

    #page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]