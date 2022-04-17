from django.urls import path
from . import views

urlpatterns = [
    path('create-event/', views.create_event, name='create-event'),
    path('event/<event_id>', views.event, name='event'),
]
