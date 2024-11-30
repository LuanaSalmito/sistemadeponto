from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions.todos import TodosPodemVer, TodosPodemCriar
from api.models.regimejornada import RegimeJornada
from api.serializers.regimejornada import RegimeJornadaSerializer

class RegimeJornadaViewSet(viewsets.ModelViewSet):
    permission_classes = [TodosPodemVer | TodosPodemCriar]
    queryset = RegimeJornada.objects.all()
    serializer_class = RegimeJornadaSerializer
    ordering_fields = ['descricao', 'horas_trabalho', 'pausa_minima']
    ordering = ['descricao']
    filterset_fields = ['descricao', 'horas_trabalho', 'pausa_minima']
    search_fields = ['descricao']

class RegimeJornadaList(APIView):
    def get(self, request):
        regimes = RegimeJornada.objects.all()
        serializer = RegimeJornadaSerializer(regimes, many=True)
        return Response(serializer.data)
