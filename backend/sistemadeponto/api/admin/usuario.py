from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models.usuario import Usuario

@admin.register(Usuario)
class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ("username", "email", "nome", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "nome")}),
        ("Permissões", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login", "date_joined", "data_criacao")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "nome", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
    )
    search_fields = ("username", "email", "nome")
    ordering = ("username",)
