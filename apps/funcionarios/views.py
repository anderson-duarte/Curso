from django.contrib.auth.models import User
from .form import FuncionarioForm
from django.urls import reverse_lazy
from django.views.generic import (UpdateView,
                                  ListView,
                                  DeleteView,
                                  CreateView)
from .models import Funcionario
import io
from django.http import FileResponse, HttpResponse


class EditarFuncionario(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'

    def get_form_kwargs(self):
        kwargs = super(EditarFuncionario, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa)


class DeletaFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:funcionarios_list')


class FuncionariosNovo(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/novo.html'
    success_url = '/funcionarios/'

    def get_form_kwargs(self):
        kwargs = super(FuncionariosNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


    def form_valid(self, form):
        funcionario = form.save(commit=False)
        usuario = funcionario.nome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create_user(username=usuario)
        return super(FuncionariosNovo, self).form_valid(form)


def some_view(request):
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, 'Hello World!')

    palavras = ['palavra1', 'palavra2', 'pallavra3']

    y=790

    for palavra in palavras:
        p.drawString(10, y, palavra)
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response