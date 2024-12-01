from django.contrib import admin
from api.models.tipojornada import TipoJornada

class TipoJornadaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'horas_regime', 'pausa_obrigatoria')
    search_fields = ('descricao',)
    list_filter = ('pausa_obrigatoria',)
    ordering = ('descricao',)

admin.site.register(TipoJornada, TipoJornadaAdmin)
