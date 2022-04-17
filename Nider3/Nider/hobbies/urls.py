from django.urls import path
from . import views

urlpatterns = [
    path('category/<category_id>', views.category, name='category'),
    path('add_hobby/<hobby_id>', views.add_hobby, name='add_hobby'),
    path('remove_hobby/<hobby_id>', views.remove_hobby, name='remove_hobby'),
]
