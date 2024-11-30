from django.contrib import admin
from api.models.registroponto import RegistroPonto

@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'data_hora', 'tipo')  
    list_filter = ('tipo', 'data_hora')  
    search_fields = ('colaborador__usuario__nome', 'tipo') 
    date_hierarchy = 'data_hora'  
