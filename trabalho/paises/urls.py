# paises/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/',views.sobre, name = 'sobre')  # Certifique-se de que a URL está corretamente configurada
]
