from django import forms
from django.forms import ModelForm
from .models import Event


class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'address', 'date', 'hobby']
