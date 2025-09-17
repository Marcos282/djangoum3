from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUsuarioCreationForm, CustomUsuarioChangeForm
from .models import CustomUsuarios

@admin.register(CustomUsuarios) # Registra o modelo CustomUsuarios no admin

class CustomUsuariosAdmin(UserAdmin):
    add_form = CustomUsuarioCreationForm
    form = CustomUsuarioChangeForm
    model = CustomUsuarios
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active','fone')
    list_filter = ('is_staff', 'is_active',)
    
    # Define a organização dos campos no admin
    fieldsets = ( 
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'data_joined')}),
    )
    
    # Define a organização dos campos ao adicionar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'fone', 'password1', 'password2', 'is_staff', 'is_active','is_superuser', 'groups')}
        ),
    )
    search_fields = ('email',) # Campo de busca
    ordering = ('email',) # Ordenação padrão