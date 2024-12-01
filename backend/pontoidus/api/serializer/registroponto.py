# app/serializers/registro_ponto.py
from rest_framework import serializers
from api.models.registroponto import RegistroPonto

class RegistroPontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPonto
        fields = ['id', 'jornada', 'hora_entrada', 'hora_saida', 'tipo_ponto', 'comentario']

    def validate(self, data):
        
        if not data.get('validar_hora'):
            raise serializers.ValidationError("A duração do ponto excede as horas previstas.")
        return data
