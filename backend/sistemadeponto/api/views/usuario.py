from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from api.models.usuario import Usuario
from api.permissions.todos import TodosPodemCriar
from api.serializers.usuario import UsuarioSerializer
from api.serializers.login import LoginSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated | TodosPodemCriar]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            
            
            user_data = UsuarioSerializer(user).data

            return Response({
                "token": token.key,
                "user": user_data
            })
        
        
        return Response({"error": "Credenciais inválidas."}, status=400)

   
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            request.user.auth_token.delete()  
            return Response({"detail": "Logout realizado com sucesso."}, status=200)
        except Exception:
            return Response({"error": "Erro ao realizar logout."}, status=400)


    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def criar_usuario(self, request):
 
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
         
            user = serializer.save()
            user.set_password(request.data['password']) 
            user.save()
            
            
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": UsuarioSerializer(user).data
            })
        
        
        return Response(serializer.errors, status=400)
