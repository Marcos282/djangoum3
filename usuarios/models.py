from django.db import models

#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager

"""
Quais as diferenças entre AbstractBaseUser e AbstractUser?
AbstractBaseUser é uma classe base que fornece a funcionalidade mínima necessária para criar um modelo de usuário personalizado. Ela inclui campos básicos como senha e métodos para autenticação, mas não inclui campos adicionais como nome, email, etc. Você precisa definir esses campos e a lógica de autenticação por conta própria.
AbstractUser, por outro lado, é uma subclasse de AbstractBaseUser que já inclui campos comuns como username, first_name, last_name, email, is_staff, is_active, date_joined, entre outros. Ele também fornece implementações padrão para métodos de autenticação. Se você precisa apenas adicionar alguns campos extras ao modelo de usuário padrão do Django, usar AbstractUser é mais simples e rápido.
"""

"""
O que é BaseUserManager?
BaseUserManager é uma classe base fornecida pelo Django que facilita a criação de gerenciadores personalizados para modelos de usuário. Ela oferece métodos úteis para criar usuários e superusuários, garantindo que os campos obrigatórios sejam preenchidos corretamente e que as senhas sejam armazenadas de forma segura.
Ao criar um modelo de usuário personalizado, é comum também criar um gerenciador personalizado que herda de BaseUserManager. Isso permite que você defina métodos específicos para criar usuários com os campos personalizados do seu modelo, além de garantir que a lógica de criação de usuários seja consistente e reutilizável. 
Por exemplo, você pode criar um método create_user que aceita parâmetros adicionais específicos do seu modelo de usuário e um método create_superuser para criar superusuários com privilégios administrativos. 
Veja um exemplo básico de como criar um gerenciador personalizado usando BaseUserManager:

 
"""

class UsuariosManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
  
        if not email:
            raise ValueError('O email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self._create_user(email, password, **extra_fields)
        

class CustomUsuarios(AbstractUser):

    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15, blank=True, null=True)
    is_staff = models.BooleanField('Membro da equipe', default=True )  # Pode acessar o admin

    USERNAME_FIELD = 'email' # Define o campo de autenticação
    REQUIRED_FIELDS = ['first_name','last_name','fone']  # Email e senha são obrigatórios por padrão

    def __str__(self):
        return self.email
    
    objects = UsuariosManager() # Define o gerenciador personalizado que será usado para criar usuários


