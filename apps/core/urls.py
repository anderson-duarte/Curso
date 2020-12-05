from django.urls import path

from . import views

app_name = 'coracao'



urlpatterns = [
    path('', views.home, name='index'),
    path('sair/', views.sair, name='sair'),
]