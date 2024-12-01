from rest_framework import serializers
from api.models.jornada import Jornada

class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = ['id', 'user', 'data', 'tipo_jornada', 'total_horas', 'horas_excedentes', 'horas_faltantes']


    def validate(self, attrs):
        
        if attrs.get('total_horas') < 0:
            raise serializers.ValidationError("Total de horas não pode ser negativo.")
        return attrs
