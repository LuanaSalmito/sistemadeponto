from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.colaborador import RegimeJornadaViewSet

router = DefaultRouter()
router.register(r'regimes-jornada', RegimeJornadaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
