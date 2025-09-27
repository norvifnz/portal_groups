from django.db import models

# Create your models here.
# app: events
# models.py
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
