from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='speakers')
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    cover = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, null=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='events', blank=True)
    published = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    # # Define many-to-many relationship with User model
    
    def get_absolute_url(self):
        return reverse('event.single', args=[self.slug])


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)
   

    class Meta:
       ordering = ['-published']
    
    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
     

class Ticket(models.Model):
    TICKET_TYPES = (
        ('GA', 'General Admission'),
        ('VIP', 'VIP'),
        ('VVIP', 'VVIP'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=4, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.ticket_type} ticket for {self.event.title}"

