from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)             #store a small amount of text
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
        # add an owner field to Topic, which establishes a foreign key relationship to the User model. 
        # If a user is deleted, all the topics associated with that user will be deleted as well

    def __str__(self):                                  #method that returns the string stored in the text attribute
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
                                #Foreign key is a
                                #database term; a reference to another record in the database. This is the
                                #code that connects each entry to a specific topic. Each topic is assigned a
                                #key, or ID, when it's created. When Django needs to establish a connection
                                #between two pieces of data, it uses the key associated with each piece of
                                #information. We'll use these connections shortly to retrieve all the entries
                                #associated with a certain topic.
                                
                                #on_delete=models.CASCADE argument tells Django that when a topic is deleted,
                                #all the entries associated with that topic should be deleted as well.
                                #This is known as a cascading delete.
                                
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' #Without this, Django would refer to multiple entries as Entrys.

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text