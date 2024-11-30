from rest_framework import serializers
from api.models.resumojornada import ResumoJornada

class ResumoJornadaSerializer(serializers.ModelSerializer):
    colaborador_nome = serializers.CharField(source='colaborador.usuario.nome', read_only=True)

    class Meta:
        model = ResumoJornada
        fields = [
            'id', 'colaborador', 'colaborador_nome', 'data', 
            'horas_trabalhadas', 'horas_extras', 'jornada_completa'
        ]
        read_only_fields = ['id', 'horas_trabalhadas', 'horas_extras', 'jornada_completa']
