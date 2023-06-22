from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Attendee, Organizer, User


class AttendeeSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_attendee = True
        user.save()
        attendee = Attendee.objects.create(user=user)
        return user


class OrganizerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_organizer = True
        user.save()
        organizer = Organizer.objects.create(user=user)
        
        organizer.save()
        return organizer