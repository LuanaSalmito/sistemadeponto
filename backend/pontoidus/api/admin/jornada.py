from django.contrib import admin
from api.models.jornada import Jornada

class JornadaAdmin(admin.ModelAdmin):
    list_display = ('user', 'data', 'tipo_jornada', 'total_horas', 'horas_excedentes', 'horas_faltantes')
    search_fields = ('user__username', 'data', 'tipo_jornada__descricao')
    list_filter = ('tipo_jornada', 'data')
    ordering = ('-data',)  

admin.site.register(Jornada, JornadaAdmin)
