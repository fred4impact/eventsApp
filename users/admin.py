from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from events.models import *



# Register the Event model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',), }
  


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'photo','url')
    list_filter = ('name', )
   

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer', 'is_published', 'is_featured', 'published')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'description', 'location')
    list_filter = ('title','speakers','date')
    # date_hierarchy = 'date'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'ticket_type', 'price', 'quantity')
    list_filter = ('event','price','ticket_type')
    search_fields = ('event', 'ticket_type', 'price')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'attendee', 'registration_date')

# Register the Attendee model
@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
    list_filter = ('user', )


# Register the Organizer model
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user', )


# Register the User model
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'is_attendee', 'is_active')
    list_filter = ('is_attendee', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

