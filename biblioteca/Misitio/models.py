from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    