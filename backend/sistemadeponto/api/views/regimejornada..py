from api.permissions.todos import TodosPodemVer
from rest_framework import viewsets
from api.models.regimejornada import RegimeJornada
from api.serializers.regimejornada import RegimeJornadaSerializer

class RegimeJornadaViewSet(viewsets.ModelViewSet):
    permissions_classes = TodosPodemVer
    queryset = RegimeJornada.objects.all()
    serializer_class = RegimeJornadaSerializer
    ordering_fields = ['descricao', 'horas_trabalho', 'pausa_minima']
    ordering = ['descricao']
    filterset_fields = ['descricao', 'horas_trabalho', 'pausa_minima']
    search_fields = ['descricao']
