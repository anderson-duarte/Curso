from django.urls import path
from . import views

app_name='departamento'

urlpatterns = [
    path('', views.DepartamentosList.as_view(), name='list_departamento'),
    path('novo/', views.DepartamentosNew.as_view(), name='novo_departamento'),
    path('editar/<int:pk>/', views.DepartamentosEdit.as_view(), name='editar_departamento'),
    path('deletar/<int:pk>/', views.DepartamentoDelete.as_view(), name='deletar_departamento'),
]