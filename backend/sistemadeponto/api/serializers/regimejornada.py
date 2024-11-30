from rest_framework import serializers
from api.models.regimejornada import RegimeJornada

class RegimeJornadaSerializer(serializers.ModelSerializer):
    jornada_prevista = serializers.SerializerMethodField()
    pausa_minima_timedelta = serializers.SerializerMethodField()

    class Meta:
        model = RegimeJornada
        fields = [
            'id',
            'descricao',
            'horas_trabalho',
            'pausa_minima',
            'jornada_prevista',
            'pausa_minima_timedelta'
        ]

    def get_jornada_prevista(self, obj):
        
        return obj.calcular_jornada_prevista().total_seconds() // 3600 
    def get_pausa_minima_timedelta(self, obj):
        
        return obj.calcular_pausa_minima().total_seconds() // 60  

    def validate_horas_trabalho(self, value):
        
        if value <= 0 or value > 24:
            raise serializers.ValidationError("As horas de trabalho devem ser entre 1 e 24.")
        return value

    def validate_pausa_minima(self, value):
        
        if value is not None and value < 0:
            raise serializers.ValidationError("A pausa mínima não pode ser negativa.")
        return value
