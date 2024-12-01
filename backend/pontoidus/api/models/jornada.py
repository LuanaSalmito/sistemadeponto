from django.db import models
from .user import User
from .tipojornada import TipoJornada


class Jornada(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    tipo_jornada = models.ForeignKey(TipoJornada, on_delete=models.CASCADE)
    total_horas = models.DecimalField(max_digits=5, decimal_places=2)
    horas_excedentes = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    horas_faltantes = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calcular_horas_excedentes(self):
        
        total_horas_trabalhadas = sum(ponto.duracao() for ponto in self.registros_ponto.all())
        jornada_com_pausa = self.total_horas + (1 if self.tipo_jornada.pausa_obrigatoria else 0)
        self.horas_excedentes = max(0, total_horas_trabalhadas - jornada_com_pausa)
        self.save()

    def calcular_horas_faltantes(self):
        total_horas_trabalhadas = sum(ponto.duracao() for ponto in self.registros_ponto.all())
        jornada_com_pausa = self.total_horas + (1 if self.tipo_jornada.pausa_obrigatoria else 0)
        self.horas_faltantes = max(0, jornada_com_pausa - total_horas_trabalhadas)
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.data}"

    def validar_jornada_completa(self):
        total_horas_trabalhadas = sum(ponto.duracao() for ponto in self.registros_ponto.all())
        jornada_com_pausa = self.total_horas + (1 if self.tipo_jornada.pausa_obrigatoria else 0)
        return total_horas_trabalhadas >= jornada_com_pausa
