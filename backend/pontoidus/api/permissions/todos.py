from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

class IsAdminOrFrontend(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_active and request.user.is_staff:
                return True
        
        referer = request.META.get('HTTP_REFERER', '')
        if 'http://localhost:8000/' in referer or 'http://localhost:3000/' in referer:
            return True
        
        return False
    
class TodosPodemVer(BasePermission):    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False

class TodosPodemCriar(BasePermission):    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        return False

class TodosPodemEditar(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT' or request.method == 'PATCH':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' or request.method == 'PATCH':
            return True
        return False

class TodosPodemDeletar(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return True
        return False

class TodosTemTodasAsPermissoes(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True
