from django.urls import path
from . import views

app_name = 'documentos'

urlpatterns = [
    path('novo/', views.DocumentosCreate.as_view(), name='documentocreate'),
    path('deletar/<int:pk>/', views.DocumentosDelete.as_view(), name='documentoDelete'),
    path('editar/<int:pk>/', views.DocumentosEditar.as_view(), name='documentoEditar'),
]