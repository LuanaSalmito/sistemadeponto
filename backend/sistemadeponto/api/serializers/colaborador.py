from rest_framework import serializers
from api.models.colaborador import Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['id', 'usuario', 'setor', 'funcao', 'regime_jornada']
