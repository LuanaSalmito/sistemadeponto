from django.contrib import admin
from api.models.registroponto import RegistroPonto

class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ('jornada', 'tipo_ponto', 'hora_entrada', 'hora_saida', 'hora_pausa', 'volta_pausa', 'horas_devidas', 'data_registro')
    search_fields = ('jornada__user__username', 'tipo_ponto')
    list_filter = ('tipo_ponto', 'jornada')
    ordering = ('-data_registro',) 

admin.site.register(RegistroPonto, RegistroPontoAdmin)
