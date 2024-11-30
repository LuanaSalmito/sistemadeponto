from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.resumojornada import ResumoJornadaViewSet

router = DefaultRouter()
router.register(r'resumos-jornada', ResumoJornadaViewSet, basename='resumo-jornada')

urlpatterns = [
    path('', include(router.urls)),
]
