from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from events.views import OrganizerDashboardView

# app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('attendee/signup/', AttendeeSignUpView.as_view(), name='attendee_signup'),
    path('organizer/signup/', OrganizerSignUpView.as_view(), name='organizer_signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
   # path('dashboard/', LogoutView.as_view, name='logout'), 
    path('dashboard/', attendee_dashboard, name='dashboard'),
    path('organizer/dashboard/', OrganizerDashboardView.as_view(), name='organizer_dashboard'),
]

