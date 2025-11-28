from django.db import models
from django.forms import CharField

# Create your models here.
class Topic(models.Model):
    """A topic a user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the string repesentation of the model"""
        return self.text
    

class Entry(models.model):
    