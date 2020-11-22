from django.urls import path
from . import views

app_name='funcionarios'

urlpatterns = [
    path('edit/<int:pk>/', views.EditarFuncionario.as_view(), name='edit_funcionario'),
    path('delete/<int:pk>/', views.DeletaFuncionario.as_view(), name='delete_funcionario'),
    path('', views.FuncionariosList.as_view(), name='funcionarios_list'),
    path('novo/', views.FuncionariosNovo.as_view(), name='funcionarios_novo'),
]