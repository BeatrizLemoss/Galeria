# paises/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Certifique-se de que a URL está corretamente configurada
]
