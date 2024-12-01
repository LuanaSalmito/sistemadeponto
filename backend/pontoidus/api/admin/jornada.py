from django.contrib import admin
from api.models.jornada import Jornada

class JornadaAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'user', 'total_horas', 'data', 'descricao')
    
    list_filter = ('user', 'data')

    list_editable = ('total_horas',)

    
    search_fields = ('descricao', 'user__username')

    ordering = ('-data',)

    
    fields = ('user', 'data', 'total_horas', 'descricao')

    fieldsets = (
        (None, {
            'fields': ('user', 'descricao', 'data')
        }),
        ('Horas', {
            'fields': ('total_horas',)
        }),
    )

admin.site.register(Jornada, JornadaAdmin)
