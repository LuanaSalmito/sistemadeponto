from django.db import models

class TipoJornada(models.Model):
    DESCRICAO_CHOICES = [
        ('6h', '6 Horas Contínuas'),
        ('8h', '8 Horas com Pausa'),
    ]

    descricao = models.CharField(max_length=255, choices=DESCRICAO_CHOICES)
    horas_regime = models.DecimalField(max_digits=5, decimal_places=2)
    pausa_obrigatoria = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao
