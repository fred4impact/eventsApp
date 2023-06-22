# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models  import User
from django.shortcuts import redirect
from .models import Attendee, Organizer, User
from django.views.generic import CreateView
from .forms import AttendeeSignUpForm, OrganizerSignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    count = User.objects.count()
    return render(request,'index.html', {'count':count})

    
class AttendeeSignUpView(CreateView):
    model = User
    form_class = AttendeeSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'attendee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class OrganizerSignUpView(CreateView):
    model = User
    form_class = OrganizerSignUpForm
    template_name = 'organizer-signup.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'organizer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')


@login_required
def attendee_dashboard(request):
    return render(request,'dashboard/attendee_board.html')



@login_required
def organizer_dashboard(request):
    return render(request,'dashboard/organizer.html')