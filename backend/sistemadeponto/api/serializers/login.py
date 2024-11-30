from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        username = data.get('username') 
        password = data.get('password')  

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Usuário está inativo.")
                return user 
            raise serializers.ValidationError("Credenciais inválidas.")
        raise serializers.ValidationError("Username e password são obrigatórios.")  
