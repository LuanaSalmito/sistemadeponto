from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.tipojornada import TipoJornadaViewSet


router = DefaultRouter()
router.register(r'tipo_jornadas', TipoJornadaViewSet, basename='tipo_jornada')


urlpatterns = [
    path('', include(router.urls)), ]
