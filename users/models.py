# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from events.models import Event


class User(AbstractUser):
    is_attendee = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)


class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
    primary_key=True, related_name='attendee')
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    registered_events = models.ManyToManyField(Event, blank=True,related_name='event_attendee')


class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='organiser')
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    organized_events = models.ManyToManyField(Event, blank=True, related_name='event_organizer')
    
