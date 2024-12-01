from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.user import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)), 
]