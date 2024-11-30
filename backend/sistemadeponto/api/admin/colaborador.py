from django.contrib import admin
from api.models.colaborador import Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'setor', 'funcao', 'regime_jornada')
    search_fields = ('usuario__nome', 'setor', 'funcao')
    list_filter = ('setor', 'funcao', 'regime_jornada')
