from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.models.jornada import Jornada
from api.serializers.jornada import JornadaSerializer

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from api.permissions.todos import TodosPodemCriar, TodosPodemVer
class JornadaViewSet(viewsets.ModelViewSet):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer
    permission_classes = [IsAuthenticated | TodosPodemVer | TodosPodemCriar]

    def get_queryset(self):
        user = self.request.user
        return Jornada.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_horas(self, request, pk=None):
        jornada = self.get_object()
        horas_adicionais = request.data.get('horas_adicionais', 0)

        if horas_adicionais < 0:
            return Response({"detail": "Horas adicionais não podem ser negativas."},
                            status=status.HTTP_400_BAD_REQUEST)

        jornada.total_horas += horas_adicionais
        jornada.save()

        return Response(JornadaSerializer(jornada).data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def atualizar_horas(self, request, pk=None):
        jornada = self.get_object()
        horas_novas = request.data.get('horas_novas', 0)

        if horas_novas < 0:
            return Response({"detail": "Horas não podem ser negativas."},
                            status=status.HTTP_400_BAD_REQUEST)

        jornada.total_horas = horas_novas
        jornada.save()

        return Response(JornadaSerializer(jornada).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def subtrair_horas(self, request, pk=None):
        jornada = self.get_object()
        horas_subtraidas = request.data.get('horas_subtraidas', 0)

        if horas_subtraidas < 0:
            return Response({"detail": "Horas subtraídas não podem ser negativas."},
                            status=status.HTTP_400_BAD_REQUEST)

        if horas_subtraidas > jornada.total_horas:
            return Response({"detail": "Não é possível subtrair mais horas do que o total registrado."},
                            status=status.HTTP_400_BAD_REQUEST)

        jornada.total_horas -= horas_subtraidas
        jornada.save()

        return Response(JornadaSerializer(jornada).data, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['get'])
    def jornadas_por_usuario(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"detail": "O parâmetro 'user_id' é obrigatório."},
                            status=status.HTTP_400_BAD_REQUEST)

        jornadas = Jornada.objects.filter(user_id=user_id)
        serializer = JornadaSerializer(jornadas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def total_horas_usuario(self, request):
        user = request.user
        total_horas = Jornada.objects.filter(user=user).aggregate(total=Sum('total_horas'))['total'] or 0
        return Response({"total_horas": total_horas}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def pesquisar_jornadas(self, request):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        
        if not data_inicio or not data_fim:
            return Response({"detail": "Parâmetros 'data_inicio' e 'data_fim' são obrigatórios."},
                            status=status.HTTP_400_BAD_REQUEST)

        jornadas = Jornada.objects.filter(data__range=[data_inicio, data_fim])
        serializer = JornadaSerializer(jornadas, many=True)
        return Response(serializer.data)


