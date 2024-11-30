from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="E-mail", max_length=255, unique=True)
    nome = models.CharField(verbose_name="Nome completo", max_length=150)
    ativo = models.BooleanField(verbose_name="Ativo", default=True)
    is_staff = models.BooleanField(verbose_name="Administrador", default=False)
    data_criacao = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome
