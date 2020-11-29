from django.shortcuts import render
from django.urls import reverse_lazy

from .models import RegistroHoraExtra
from .form import HoraExtraForm
from apps.funcionarios.models import Funcionario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class HorasExtrasCreate(CreateView):
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = '/funcionarios/'

    def get_form_kwargs(self):
        kwargs = super(HorasExtrasCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class HorasExtrasEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('horas_extras:horas_extras-lista')

    def get_form_kwargs(self):
        kwargs = super(HorasExtrasEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HorasExtrasDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('horas_extras:horas_extras-lista')