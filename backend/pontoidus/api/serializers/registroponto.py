from rest_framework import serializers
from api.models.registroponto import RegistroPonto
from datetime import timedelta

class RegistroPontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPonto
        fields = '__all__'
    
    def validate(self, data):
        """Aqui você pode adicionar validações customizadas para garantir a consistência dos campos"""
        if data.get('tipo_ponto') == RegistroPonto.PAUSA and not data.get('hora_pausa'):
            raise serializers.ValidationError("Hora de pausa é obrigatória.")
        return data

    def update(self, instance, validated_data):
        """Aqui você pode implementar qualquer lógica extra para atualização, como o cálculo de débitos"""
        instance = super().update(instance, validated_data)
        instance.calcular_debitos() 
        return instance
