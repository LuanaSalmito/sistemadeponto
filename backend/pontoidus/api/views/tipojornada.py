from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.models.tipojornada import TipoJornada
from api.serializers.tipojornada import TipoJornadaSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class TipoJornadaViewSet(viewsets.ModelViewSet):
    queryset = TipoJornada.objects.all()
    serializer_class = TipoJornadaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
      
        return TipoJornada.objects.all()

    def perform_create(self, serializer):
      
        serializer.save()

    @action(detail=True, methods=['post'])
    def atualizar_pausa(self, request, pk=None):
        tipo_jornada = self.get_object()
        pausa_obrigatoria = request.data.get('pausa_obrigatoria')

        if pausa_obrigatoria is None:
            return Response({"detail": "O campo 'pausa_obrigatoria' é obrigatório."},
                            status=status.HTTP_400_BAD_REQUEST)

        tipo_jornada.pausa_obrigatoria = pausa_obrigatoria
        tipo_jornada.save()

        return Response(TipoJornadaSerializer(tipo_jornada).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def detalhes_completo(self, request, pk=None):
        tipo_jornada = self.get_object()
        
        data = {
            "descricao": tipo_jornada.descricao,
            "horas_regime": tipo_jornada.horas_regime,
            "pausa_obrigatoria": tipo_jornada.pausa_obrigatoria,
            "detalhes_adicionais": "Aqui você pode adicionar mais informações."
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def jornada_colaborador(self, request):
        
        colaborador_id = request.query_params.get('colaborador_id')

        if not colaborador_id:
            return Response({"detail": "O parâmetro 'colaborador_id' é obrigatório."},
                            status=status.HTTP_400_BAD_REQUEST)

       
        tipo_jornadas = TipoJornada.objects.filter(colaborador_id=colaborador_id)
        
        if not tipo_jornadas:
            return Response({"detail": "Nenhuma jornada encontrada para este colaborador."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TipoJornadaSerializer(tipo_jornadas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def total_jornadas(self, request):
    
        total = TipoJornada.objects.count()
        return Response({"total_jornadas": total}, status=status.HTTP_200_OK)
