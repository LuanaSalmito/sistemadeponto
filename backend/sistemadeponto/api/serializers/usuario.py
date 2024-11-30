from rest_framework import serializers
from api.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'nome', 'ativo', 'data_criacao', 'password']
        read_only_fields = ['data_criacao']  

    def create(self, validated_data):
        
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            nome=validated_data.get('nome', ''),
            ativo=validated_data.get('ativo', True),  
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.ativo = validated_data.get('ativo', instance.ativo)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance
