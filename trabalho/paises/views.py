# paises/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def descricao(request):
    return render(request, 'descricao.html')

from django.utils import timezone
from datetime import time
from django.shortcuts import render

def hora_aula(req):
    
    agora = timezone.localtime().time()  

   
    inicio_aula = time(9, 30)  # 9:30
    fim_aula = time(11, 40)    # 11:40

   
    hora = inicio_aula <= agora <= fim_aula

    return render(req, 'hora_aula.html', {'hora': hora})
