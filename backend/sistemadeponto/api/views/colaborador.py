from rest_framework import viewsets
from api.models.colaborador import Colaborador
from api.permissions.todos import TodosPodemVer
from api.serializers.colaborador import ColaboradorSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    permission_classes = [TodosPodemVer]
    search_fields = ['usuario__nome', 'setor', 'funcao']
    list_filter = ['setor', 'funcao', 'regime_jornada']
    ordering_fields = ['usuario__nome', 'setor', 'funcao']
    ordering = ['usuario__nome']
    filterset_fields = ['setor', 'funcao']

