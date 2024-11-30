from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.registroponto import RegistroPontoViewSet

router = DefaultRouter()
router.register(r'registros', RegistroPontoViewSet, basename='registro-ponto')

urlpatterns = [
    path('', include(router.urls)),
]
