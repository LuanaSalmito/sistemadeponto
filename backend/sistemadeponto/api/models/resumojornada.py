from datetime import timedelta
from django.db import models


class ResumoJornada(models.Model):
    colaborador = models.ForeignKey('Colaborador', on_delete=models.CASCADE, related_name="resumos")
    data = models.DateField(verbose_name="Data")
    horas_trabalhadas = models.DurationField(verbose_name="Horas Trabalhadas", default=timedelta)
    horas_extras = models.DurationField(verbose_name="Horas Extras", default=timedelta)
    jornada_completa = models.BooleanField(verbose_name="Jornada Completa", default=False)

    class Meta:
        verbose_name = "Resumo de Jornada"
        verbose_name_plural = "Resumos de Jornada"

    def __str__(self):
        return f"{self.colaborador.usuario.nome} - {self.data}"

    def calcular_resumo(self):
        registros = self.colaborador.registros.filter(data_hora__date=self.data).order_by("data_hora")
        total = timedelta()

        
        for i in range(0, len(registros) - 1, 2):
            entrada = registros[i].data_hora
            saida = registros[i + 1].data_hora
            total += saida - entrada

        self.horas_trabalhadas = total

        
        jornada_prevista = timedelta(hours=self.colaborador.regime_jornada.horas_trabalho)
        if total >= jornada_prevista:
            self.jornada_completa = True
            self.horas_extras = total - jornada_prevista
        else:
            self.jornada_completa = False
            self.horas_extras = timedelta()

        self.save()
