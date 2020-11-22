from django.urls import path
from . import views

app_name = 'horas_extras'

urlpatterns = [
    path('', views.HorasExtrasList.as_view(), name='horas_extras-lista'),
    path('adicionar/', views.HorasExtrasCreate.as_view(), name='horas_extras-add'),
    path('editar/<int:pk>/', views.HorasExtrasEdit.as_view(), name='horas_extras_edit'),
    path('delletar/<int:pk>/', views.HorasExtrasDelete.as_view(), name='horas_extras_delete'),
]