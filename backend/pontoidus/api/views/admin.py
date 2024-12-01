from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api.models.user import User
from api.serializers.user import UserSerializer
from rest_framework.decorators import action

class AdminViewSet(viewsets.ModelViewSet):
    """
    ViewSet para administração de colaboradores.
    Só administradores têm acesso a essas ações.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
      
        return User.objects.filter(tipo_usuario=User.COLABORADOR)


    @action(detail=False, methods=['get'], url_path='colaboradores')
    def list_colaboradores(self, request):
        colaboradores = self.get_queryset()
        serializer = self.serializer_class(colaboradores, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['post'], url_path='criar-colaborador')
    def create_colaborador(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
           
            serializer.validated_data['tipo_usuario'] = User.COLABORADOR
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    @action(detail=True, methods=['put'], url_path='editar-colaborador')
    def update_colaborador(self, request, pk=None):
        try:
            colaborador = User.objects.get(pk=pk, tipo_usuario=User.COLABORADOR)
        except User.DoesNotExist:
            return Response({"error": "Colaborador não encontrado"}, status=404)

        serializer = self.serializer_class(colaborador, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    @action(detail=True, methods=['delete'], url_path='excluir-colaborador')
    def delete_colaborador(self, request, pk=None):
        try:
            colaborador = User.objects.get(pk=pk, tipo_usuario=User.COLABORADOR)
        except User.DoesNotExist:
            return Response({"error": "Colaborador não encontrado"}, status=404)
        
        colaborador.delete()
        return Response({"message": "Colaborador excluído com sucesso"}, status=200)
