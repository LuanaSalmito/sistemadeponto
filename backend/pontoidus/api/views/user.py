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

    # Endpoint para criar conta
    @action(detail=False, methods=['post'], url_path='criar-conta')
    def create_account(self, request):
        # Permitir somente admins criarem contas
        if not request.user.is_staff:  # Verifica se o usuário não é admin
            return Response({"error": "Permissão negada. Somente administradores podem criar contas."}, status=status.HTTP_403_FORBIDDEN)

        # Verifica se a conta admin já existe
        if User.objects.filter(username="admin").exists():
            return Response({"message": "Usuário admin já existe."}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        
        if username == "admin" and password == "123456":
            
            user = User.objects.create_superuser(username="admin", password="123456", email="admin@dominio.com")
            user.save()
            return Response({"message": "Conta de admin criada com sucesso"}, status=status.HTTP_201_CREATED)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['post'], url_path='logout')
    def logout_user(self, request):
        logout(request)
        return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)
