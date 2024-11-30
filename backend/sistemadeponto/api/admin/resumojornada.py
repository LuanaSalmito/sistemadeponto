from django.contrib import admin
from api.models.resumojornada import ResumoJornada

@admin.register(ResumoJornada)
class ResumoJornadaAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'data', 'horas_trabalhadas', 'horas_extras', 'jornada_completa')
    list_filter = ('jornada_completa', 'data')
    search_fields = ('colaborador__usuario__nome',)
