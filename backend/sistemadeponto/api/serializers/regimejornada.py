from rest_framework import serializers
from api.models.regimejornada import RegimeJornada


class RegimeJornadaSerializer(serializers.ModelSerializer):
    jornada_prevista = serializers.DurationField(source='calcular_jornada_prevista', read_only=True)
    pausa_minima_calculada = serializers.DurationField(source='calcular_pausa_minima', read_only=True)

    class Meta:
        model = RegimeJornada
        fields = ['id', 'descricao', 'horas_trabalho', 'pausa_minima', 'jornada_prevista', 'pausa_minima_calculada']
