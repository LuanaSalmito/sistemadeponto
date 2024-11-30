from django.db import models
from api.models.colaborador import Colaborador
class RegistroPonto(models.Model):

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="registros")
    data_hora = models.DateTimeField(verbose_name="Data e Hora do Registro")
    tipo = models.CharField(
        verbose_name="Tipo de Registro",
        max_length=10,
        choices=(("entrada", "Entrada"), ("saida", "Saída")),
    )

    class Meta:
        verbose_name = "Registro de Ponto"
        verbose_name_plural = "Registros de Ponto"

    def __str__(self):
        return f"{self.colaborador.usuario.nome} - {self.tipo} em {self.data_hora}"
