from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.registroponto import RegistroPonto
from api.serializers.registroponto import RegistroPontoSerializer
from rest_framework import status

class RegistroPontoViewSet(viewsets.ModelViewSet):
    queryset = RegistroPonto.objects.all()
    serializer_class = RegistroPontoSerializer

    def list(self, request, *args, **kwargs):
        """
        Listar todos os registros de ponto.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Criar um novo registro de ponto.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Lógica de cálculo ou validação adicional, se necessário
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Atualizar um registro de ponto existente.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Deletar um registro de ponto.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def calcular_debitos(self, request, pk=None):
        """
        Ação customizada para calcular os débitos de horas de um registro de ponto.
        """
        registro = self.get_object()
        registro.calcular_debitos()
        return Response({'status': 'débitos calculados', 'horas_devidas': str(registro.horas_devidas)})
