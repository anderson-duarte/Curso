from django.urls import path
from . import views

app_name = 'empresas'

urlpatterns = [
    path('nova/', views.CriarEmpresa.as_view(), name='criar_empresa'),
    path('editar/<int:pk>/', views.EditarEmpresa.as_view(), name='editar_empresa'),
]