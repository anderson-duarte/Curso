from rest_framework import serializers
from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'hora_extra']