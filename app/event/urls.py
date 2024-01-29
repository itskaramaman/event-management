from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create-event'),
    path('events/user/', views.user_events, name='user-events'),
    path('events/<slug:slug>/', views.event_details, name='event-details'),
]
