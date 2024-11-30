from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers.login import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
