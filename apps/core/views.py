from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.core.serializers import UserSerializer, GroupSerializer

# Create your views here.

@login_required
def home(request):
    usuario = request.user
    contexto = {'usuario':usuario}
    return render(request, 'core/home.html', contexto)


def sair(request):
    return render(request, 'core/logout.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by()
    serializer_class = GroupSerializer