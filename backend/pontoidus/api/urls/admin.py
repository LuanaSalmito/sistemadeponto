from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.admin import AdminViewSet


router = DefaultRouter()
router.register(r'admin', AdminViewSet, basename='admin')

urlpatterns = [
    path('', include(router.urls)), 
]
