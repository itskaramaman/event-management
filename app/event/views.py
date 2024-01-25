from django.shortcuts import render, redirect
from .models import Event
from .form import EventForm


def home(request):
    """
    Get the near by and online events
    """
    online_events = Event.objects.filter(
        online=True
    ).order_by('-created_at')[:4]
    return render(request, 'event/home.html', {'online_events': online_events})


def create_event(request):
    """
    Create Event
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # import ipdb;ipdb.set_trace()
            form.instance.organizer_id = request.user.id
            form.save()
            return redirect('/')
    form = EventForm()
    return render(request, 'event/create.html', {'form': form})
