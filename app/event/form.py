from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'starts_at', 'ends_at', 'online',
                  'location', 'categories', 'capacity', 'price',
                  'registeration_deadline', 'image', 'status', 'external_link']
        widgets = {
            'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ends_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'registeration_deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(

            Div(
                'title'
              ),
            Div(
                'description'
              ),
            Div(
                'starts_at', 'ends_at',
                css_class='grid grid-cols-2 gap-4'
            ),
            Div(
                'online', 'location', 'categories', 'tags',
                css_class='grid grid-cols-2 gap-4'
            ),
            Div(
                'organizer', 'capacity', 'registeration_deadline',
                css_class='grid grid-cols-2 gap-4'
            ),
            Div(
                'price', 'image', 'status', 'external_link',
                css_class='grid grid-cols-2 gap-4'
            ),
        )
