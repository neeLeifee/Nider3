from django.contrib import messages
from .forms import SignUpForm, LoginForm, EditUserForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            city = profile_form.cleaned_data['city']
            gender = profile_form.cleaned_data['gender']
            new_profile = Profile(user=new_user, city=city, gender=gender)
            new_profile.save()
            return redirect('/')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/sign-up.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Не удалось найти пользователя с такими логином или паролем",
                               extra_tags='alert alert-warning alert-dismissible fade show')
    else:
        form = LoginForm()
    context = {'form': form, 'title': 'Вход'}
    return render(request, 'users/login.html', context)


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST)  # проблема: поля не автозаполняются имеющимися данными
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            _profile = Profile.objects.get(user=request.user)
            _profile.city = profile_form.cleaned_data['city']
            _profile.gender = profile_form.cleaned_data['gender']
            _profile.save()
            return redirect('/')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/edit-profile.html', context)


def profile(request, profile_user_username):
    _profile = Profile.objects.get(user__username=profile_user_username)
    context = {
        'profile': _profile,
        'my_hobbies': Profile.objects.get(user=request.user).hobbies.all(),
    }
    return render(request, 'users/profile.html', context)
