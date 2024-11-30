from rest_framework import serializers
from api.models.registroponto import RegistroPonto

class RegistroPontoSerializer(serializers.ModelSerializer):
    colaborador_nome = serializers.CharField(source='colaborador.usuario.nome', read_only=True)

    class Meta:
        model = RegistroPonto
        fields = ['id', 'colaborador', 'colaborador_nome', 'data_hora', 'tipo']
        read_only_fields = ['id']
