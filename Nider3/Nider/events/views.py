from django.shortcuts import render, redirect
from .models import Event
from .forms import CreateEventForm
from django.contrib.auth.decorators import login_required
from users.models import Profile


def event(request, event_id):
    """Функция для страницы конкретного события"""
    _event = Event.objects.get(pk=event_id)
    context = {
        'event': _event,
    }
    return render(request, 'event.html', context)


@login_required
def create_event(request):
    """Функция для страницы создания события"""
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            new_event.creator_name = request.user.username
            new_event.save()
            return redirect('/')
    else:
        form = CreateEventForm()
    context = {
        'form': form,
    }
    return render(request, 'create-event.html', context)


@login_required
def participate(request, event_id):  # НЕ ДОДЕЛАНО
    _event = Event.objects.get(pk=event_id)
    _profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        _event.participants.add(_profile)
        return redirect(request.path)
    context = {
        'event': _event,
    }
    return render(request, 'category.html', context)
