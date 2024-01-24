from django.shortcuts import render
from .models import Event


def home(request):
    """
    Get the near by and online events
    """
    online_events = Event.objects.filter(online=True).all()
    return render(request, 'event/home.html', {'online_events': online_events})
