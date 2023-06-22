from django import forms
from django.forms import ModelForm # newly addded
from .models import Event
from django.forms.widgets import DateInput
# from django.forms import DateTimeInput




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description','slug','cover','date','location','is_published','is_featured','category','speakers','organizer')
        


        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'Choose event date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 3, 'placeholder':'Describe your event'}),
            
        }

       

        # fields = ['title', 'description','poster','date','location','is_published','is_featured','category','published','organizer']




