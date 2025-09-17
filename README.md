# 📝 Resumo do Projeto – Usuário Customizado no Django

Este projeto implementa um **modelo de usuário customizado** no Django, permitindo maior flexibilidade na autenticação e no gerenciamento de usuários.

## 🔑 Motivos para usar um modelo customizado
- Substituir o modelo padrão de usuários do Django (`User`).
- Permitir a expansão futura com novos campos (ex: CPF, telefone, etc.).
- Melhor controle sobre autenticação e criação de contas.

---

## 📂 Estrutura e Arquivos Configurados

### **veja os arquivos princiais**
- admin.py
- forms.py
- models.py
Todos dentro do app usuarios

Também olhe o arquivo settings, pois nele foi setado uma constante que orienta o python a usar o sistema de autenticação dentro do app usuarios >> CustomUsuarios
```python
AUTH_USER_MODEL = 'usuarios.CustomUsuarios'
```

### 1. **models.py**
- Criado o modelo `CustomUsuarios`, estendendo `AbstractUser`.
- Uso do `pass` inicialmente, para manter compatibilidade com o modelo padrão e abrir espaço para futuras customizações.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUsuarios(AbstractUser):
    pass
```

---

### 2. **managers.py (opcional, se usado)**
- Caso você tenha usado `BaseUserManager` para controlar a criação de usuários:
  - Métodos `create_user` e `create_superuser` foram sobrescritos.
  - Definição de validações personalizadas (ex: obrigar e-mail).

---

### 3. **settings.py**
- Configuração da constante `AUTH_USER_MODEL` para apontar para o modelo customizado:

```python
AUTH_USER_MODEL = "app.CustomUsuarios"
```

> ⚠️ Deve ser definido **antes da primeira migração**, para evitar conflitos com o banco.

---

### 4. **admin.py**
- Registro do modelo `CustomUsuarios` no Django Admin.
- Uso de `UserAdmin` como base para manter as funcionalidades padrão do painel de administração.

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsuarios

@admin.register(CustomUsuarios)
class CustomUsuariosAdmin(UserAdmin):
    pass
```

---

## ⚙️ Outras Configurações
- **Migrations** rodadas após a criação do modelo.
- Ajustes no `superuser` criados pelo `createsuperuser` para funcionar com o modelo customizado.
- Login no Django Admin funcionando com o novo usuário customizado.

---

## ✅ Resultado Final
- O projeto agora utiliza um **usuário customizado baseado em `AbstractUser`**.  
- A autenticação, cadastro e gerenciamento de usuários funcionam normalmente no Admin.  
- A aplicação está pronta para receber novos campos no modelo de usuário sem precisar refatorar o core do projeto.

---
