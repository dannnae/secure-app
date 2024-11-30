from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Modelo de usuario personalizado
class CustomUser(AbstractUser):
    pass  # Django maneja autenticación y encriptación automáticamente

# Modelo de entradas del blog
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title