from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .form import EventForm


def home(request):
    """
    Get the near by and online events
    """
    online_events = Event.objects.filter(
        online=True,
        ends_at__gt=timezone.now()
    ).order_by('-created_at')[:4]

    offline_events = Event.objects.filter(
        online=False,
        ends_at__gt=timezone.now()
    ).order_by('-created_at')[:4]

    context = {
        'online_events': online_events,
        'offline_events': offline_events
    }
    return render(request, 'event/home.html', context)


@login_required
def create_event(request):
    """
    Create Event
    """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            form.instance.organizer_id = request.user.id
            form.save()
            return redirect('/')
    form = EventForm()
    return render(request, 'event/create.html', {'form': form})


@login_required
def user_events(request):
    """
    Current logged in user events
    """
    user_events = Event.objects.filter(
        organizer_id=request.user.id
    )

    upcoming_events = user_events.filter(
        starts_at__gt=timezone.now()
    ).order_by('-created_at').all()

    finished_events = user_events.filter(
        ends_at__lt=timezone.now()
    ).order_by('-created_at').all()

    ongoing_events = user_events.filter(
        starts_at__lte=timezone.now(),
        ends_at__gte=timezone.now()
    ).order_by('-created_at').all()

    context = {
        'upcoming_events': upcoming_events,
        'ongoing_events': ongoing_events,
        'finished_events': finished_events
    }

    return render(request, 'event/user_events.html', context)


def event_details(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event/event_details.html', {'event': event})


@login_required
def edit_event(request, id):
    """
    Create Event
    """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            form.instance.organizer_id = request.user.id
            form.save()
            return redirect('/')
    form = EventForm()
    return render(request, 'event/create.html', {'form': form})
