from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Tipos de usuário com o campo 'tipo_usuario'
    ADMIN = 'admin'
    COLABORADOR = 'colaborador'
    
    TIPOS_USUARIOS = [
        (ADMIN, 'Administrador'),
        (COLABORADOR, 'Colaborador'),
    ]

    tipo_usuario = models.CharField(
        max_length=15, choices=TIPOS_USUARIOS, default=COLABORADOR
    )

    # Usando o related_name para evitar conflito no relacionamento com 'groups'
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='custom_user_set',  # Nome único para evitar conflito com o User padrão
        blank=True
    )

    # Permissões de usuário, se necessário (personalizando como seu código original)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='%(app_label)s_%(class)s_user_permissions',  
        blank=True
    )

    def __str__(self):
        return self.username
