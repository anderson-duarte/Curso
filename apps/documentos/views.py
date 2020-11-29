from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Documento
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.


class DocumentosCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    success_url = '/funcionarios/'

    def form_valid(self, form):
        documento = form.save(commit=False)
        documento.pertence = self.request.user.funcionario
        documento.save()
        return super(DocumentosCreate, self).form_valid(form)


class DocumentosDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('documentos:documentolist')

class DocumentosEditar(UpdateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    success_url = reverse_lazy('documentos:documentolist')