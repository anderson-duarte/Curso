from django.db import models
from django.db.models import Sum

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name='Motivo')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    hora_extra = models.DecimalField(max_digits=5, decimal_places=2,
                                     verbose_name='Hora Extra', default=0);

    def __str__(self):
        return self.motivo

    @property
    def total_horas_extras(self):
        return self.registrohoraextra_set.all().aggregate(Sum('hora_extra'))['hora_extra__sum']

