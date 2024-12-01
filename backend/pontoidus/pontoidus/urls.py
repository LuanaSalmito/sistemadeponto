from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API de Regimes de Jornada",
        default_version='v1',
        description=(
            "Documentação da API para gerenciar regimes de jornada de trabalho. "
            "Inclui endpoints para CRUD e suporte a filtros, ordenação e busca."
        ),
        
        contact=openapi.Contact(email="luanasalmito@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  
)

urlpatterns = [
   
    path('admin/', admin.site.urls),
    
    path('api/', include('api.urls')),

    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
