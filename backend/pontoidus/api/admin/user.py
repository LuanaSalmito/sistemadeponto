from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models.user import User

class UserAdminCustom(UserAdmin):
    # Campos a serem exibidos na lista de usuários no admin
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Campos a serem exibidos no formulário de edição do usuário
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'tipo_usuario')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos a serem exibidos no formulário de criação do usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'tipo_usuario', 'is_staff', 'is_active'),
        }),
    )

    # Métodos adicionais
    def save_model(self, request, obj, form, change):
        obj.save()

# Registra o modelo customizado de User e o UserAdmin customizado
admin.site.register(User, UserAdminCustom)
