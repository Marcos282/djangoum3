from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUsuarios

class CustomUsuarioCreationForm(UserCreationForm):
    class Meta: # Define qual modelo o formulário irá usar
        model = CustomUsuarios # Modelo personalizado (Class based view)
        fields = ('email', 'first_name', 'last_name', 'fone')
        labels = {
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'fone': 'Telefone',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["usarname"]  # Define o email como username
        
        if commit:
            user.save()
        return user
    
class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuarios
        fields = ('email', 'first_name', 'last_name', 'fone')
