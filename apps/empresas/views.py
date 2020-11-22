from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from .models import Empresa


class CriarEmpresa(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect('/')


class EditarEmpresa(UpdateView):
    model = Empresa
    fields = ['nome']
    success_url = '/'