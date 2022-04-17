from django.shortcuts import render, redirect
from .models import Hobby, HobbyCategory
from users.models import Profile
from django.contrib.auth.decorators import login_required


def category(request, category_id):
    _category = HobbyCategory.objects.get(pk=category_id)
    _hobbies = Hobby.objects.filter(category__id=category_id)
    _profile = Profile.objects.get(user=request.user)
    _my_hobbies = _profile.hobbies.all()
    context = {
        'title': 'Категория',
        'category': _category,
        'hobbies': _hobbies,
        'my_hobbies': _my_hobbies,
    }
    return render(request, 'category.html', context)


@login_required
def add_hobby(request, hobby_id):
    _hobby = Hobby.objects.get(pk=hobby_id)
    _profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        _profile.hobbies.add(_hobby)
        return redirect('category', category_id=_hobby.category.id)  # на ту же страницу
    context = {
        'hobby': _hobby,
    }
    return render(request, 'category.html', context)


@login_required
def remove_hobby(request, hobby_id):
    _hobby = Hobby.objects.get(pk=hobby_id)
    _profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        _profile.hobbies.remove(_hobby)
        return redirect('category', category_id=_hobby.category.id)  # на ту же страницу
    context = {
        'hobby': _hobby,
    }
    return render(request, 'category.html', context)
