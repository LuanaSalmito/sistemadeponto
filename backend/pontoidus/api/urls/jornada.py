from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.jornada import JornadaViewSet

router = DefaultRouter()
router.register(r'jornadas', JornadaViewSet, basename='jornada')


urlpatterns = [
    path('', include(router.urls)), 
]
