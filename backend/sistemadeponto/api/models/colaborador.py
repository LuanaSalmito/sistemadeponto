from django.db import models
from api.models.regimejornada import RegimeJornada
from api.models.usuario import Usuario


class Colaborador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="colaborador")
    setor = models.CharField(verbose_name="Setor", max_length=100)
    funcao = models.CharField(verbose_name="Função", max_length=100)
    regime_jornada = models.ForeignKey(RegimeJornada, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.usuario.nome
