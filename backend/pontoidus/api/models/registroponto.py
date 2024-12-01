from django.db import models
from .jornada import Jornada
from api.services.calculos_jornada import CalculadoraJornada
from datetime import timedelta

class RegistroPonto(models.Model):
    ENTRADA = 'entrada'
    SAIDA = 'saida'
    PAUSA = 'pausa'

    TIPO_PONTO_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
        (PAUSA, 'Pausa'),
    ]

    jornada = models.ForeignKey(Jornada, related_name='registros_ponto', on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(null=True, blank=True)
    hora_saida = models.DateTimeField(null=True, blank=True)
    tipo_ponto = models.CharField(max_length=20, choices=TIPO_PONTO_CHOICES)
    volta_pausa = models.DateTimeField(null=True, blank=True)  
    horas_devidas = models.DurationField(default=timedelta(0))
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jornada.user.username} - {self.tipo_ponto} - {self.hora_entrada} / {self.hora_saida}"

    def calcular_debitos(self):
        """Chama a função do serviço de cálculos para calcular os débitos de horas."""
        CalculadoraJornada.atualizar_jornada(self)

    def duracao(self):
        if self.tipo_ponto == self.ENTRADA and self.hora_saida:
            return self.hora_saida - self.hora_entrada
        elif self.tipo_ponto == self.PAUSA and self.volta_pausa:
            return self.volta_pausa - self.hora_entrada
        return timedelta(0)