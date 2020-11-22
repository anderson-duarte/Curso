from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    usuario = request.user
    contexto = {'usuario':usuario}
    return render(request, 'core/home.html', contexto)


def sair(request):
    return render(request, 'core/logout.html')
