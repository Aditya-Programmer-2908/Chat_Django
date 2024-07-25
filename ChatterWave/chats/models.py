from django.db import models
from datetime import datetime

class Room(models.Model):
    name=models.CharField(max_length=1000)

class Message(models.Model):
    value = models.TextField()
    date=models.DateTimeField(default=datetime.now, blank=True)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=1000)