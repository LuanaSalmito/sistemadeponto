from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from api.models.user import User
from api.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail=False, methods=['post'], url_path='login')
    def login_user(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login bem-sucedido"}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='criar-conta')
    def create_account(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Você precisa estar logado para criar contas."}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not request.user.is_staff:
            return Response({"error": "Permissão negada. Somente administradores podem criar contas."}, status=status.HTTP_403_FORBIDDEN)

        if User.objects.filter(username="admin").exists():
            return Response({"message": "Usuário admin já existe."}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        tipo_usuario = request.data.get('tipo_usuario', User.COLABORADOR)

        if tipo_usuario not in [User.ADMIN, User.COLABORADOR]:
            return Response({"error": "Tipo de usuário inválido."}, status=status.HTTP_400_BAD_REQUEST)

        if tipo_usuario == User.ADMIN:
            return Response({"error": "Somente um administrador pode criar um usuário admin."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, tipo_usuario=User.COLABORADOR)
        
        return Response({"message": "Conta de colaborador criada com sucesso."}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout_user(self, request):
        logout(request)
        return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)
