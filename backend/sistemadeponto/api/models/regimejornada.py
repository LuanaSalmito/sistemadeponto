from datetime import timedelta
from django.db import models

class RegimeJornada(models.Model):
    descricao = models.CharField(max_length=50)
    horas_trabalho = models.PositiveIntegerField()
    pausa_minima = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Regime de Jornada"
        verbose_name_plural = "Regimes de Jornada"

    def __str__(self):
        return f"{self.descricao} ({self.horas_trabalho}h)"

    def calcular_jornada_prevista(self):
        return timedelta(hours=self.horas_trabalho)

    def calcular_pausa_minima(self):
        if self.pausa_minima:
            return timedelta(minutes=self.pausa_minima)
        return timedelta()
