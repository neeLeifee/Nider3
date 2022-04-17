from django.shortcuts import render
import folium
from hobbies.models import HobbyCategory


def home(request):
    m = folium.Map(location=[55, 88], zoom_start=3)
    folium.Marker([55.644466, 37.395744], tooltip='Click for more', popup='Moscow').add_to(m)
    m = m._repr_html_()
    context = {
        'title': 'Главная страница',
        'm': m,
        'categories': HobbyCategory.objects.all(),
    }
    return render(request, 'main/home.html', context)
