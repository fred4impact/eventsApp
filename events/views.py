from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.list import ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from events.models import Event



# Create your views here.

def home(request):
    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, 'events/allevents.html', context)



class EventList(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(Q(organizer=user) | Q(attendees=user)).distinct()


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page
            return redirect('/events') 
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form})




def show(request, id):
    event = Event.objects.get(id=id)
    context = {
        "event": event
    }
    return render(request, 'events/show.html', {'event': event})



class OrganizerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/organizer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current logged-in user
        user = self.request.user
        # Get the events created by the organizer
        events = Event.objects.filter(organizer=user)
        context['events'] = events
        return context

   


 