from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign-up', views.register_user, name='sign-up'),
    path('login', views.login_user, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<profile_user_username>', views.profile, name='profile'),
    path('edit-profile', views.edit_user, name='edit-profile'),
]
