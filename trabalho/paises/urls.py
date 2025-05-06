# paises/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/',views.sobre, name = 'sobre'),
    path('descricao/',views.descricao, name = 'descricao'),
    path('hora_aula/',views.hora_aula, name = 'hora_aula')

]
