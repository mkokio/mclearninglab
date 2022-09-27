from django.contrib import admin

# Register your models here.
from .models import Topic, Entry   #we want to register, Topic and Entry
                            #The dot tells Django to look for models.py in the same directory as admin.py.

admin.site.register(Topic)  #Tells Django to manage our model through the admin site 
admin.site.register(Entry)
