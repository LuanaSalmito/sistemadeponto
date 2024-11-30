from django.contrib import admin
from api.models.regimejornada import RegimeJornada

@admin.register(RegimeJornada)
class RegimeJornadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'horas_trabalho', 'pausa_minima')
    search_fields = ('descricao',)
    list_filter = ('horas_trabalho',)
    ordering = ('descricao',)
