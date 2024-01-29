from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed')
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    starts_at = models.DateTimeField(blank=False, null=False)
    ends_at = models.DateTimeField(blank=False, null=False)
    online = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=50, blank=True)
    registeration_deadline = models.DateTimeField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/', default='default-event.png')
    status = models.CharField(choices=EVENT_STATUS_CHOICES, default='upcoming')
    external_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class EventAttendants(models.Model):
    """
    Relationship between Event and Attendee
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}'
