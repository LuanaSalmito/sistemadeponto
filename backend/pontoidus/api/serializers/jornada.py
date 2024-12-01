
from rest_framework import serializers
from api.models.jornada import Jornada

class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'
