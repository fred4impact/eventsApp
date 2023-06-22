from django.urls import path
# from .views import *
from .views import EventList, create_event, show, OrganizerDashboardView

# app_name = 'events'


urlpatterns = [

    path('', EventList.as_view(), name='event_list'),
    path('create/', create_event, name='create_event'),
    path('<int:id>/', show, name='event_show'),
  
] 




   # path('<int:id>/edit/', edit, name='events.edit'),
    # path('<int:id>/delete/',delete, name='events.delete'),