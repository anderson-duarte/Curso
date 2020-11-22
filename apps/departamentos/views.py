from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento

# Create your views here.

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa)


class DepartamentosNew(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = '/departamentos/'

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosNew, self).form_valid(form)


class DepartamentosEdit(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = '/departamentos/'

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamento:list_departamento')

