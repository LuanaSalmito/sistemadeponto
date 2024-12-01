from rest_framework import serializers
from api.models.tipojornada import TipoJornada

class TipoJornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoJornada
        fields = ['id', 'descricao', 'horas_regime', 'pausa_obrigatoria']
