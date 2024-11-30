from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(verbose_name="Nome completo", max_length=150, blank=True, null=True)
    ativo = models.BooleanField(verbose_name="Ativo", default=True)
    data_criacao = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username
