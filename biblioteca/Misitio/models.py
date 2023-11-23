from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=80)
    editorial = models.CharField(max_length=80)
    fecha_publicacion = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    ISBN = models.BigIntegerField(max_length=13)
    resumen = models.TextField()
    
    disponible = "Disponible"
    prestado = "Prestado"
    prestamo = "Proceso de Préstamo"
    disponibilidad_choices = (
        disponible,
        prestado,
        prestamo,
    )
    
    disponibilidad = models.Choices(choices = disponibilidad_choices)
    portada = models.ImageField(upload_to=None, height_field=None, width_field=None)

class Autor():
    nombre = models.CharField(max_length=50)
    biografia = models.CharField(max_length=100)
    foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
class Editorial():
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    sitioWeb = models.URLField(max_length=70)

class Prestamo():
    libroPrestado = models.CharField(max_length=50)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField()
    usuario = models.CharField(max_length=50)
    
    prestado = "prestado"
    devuelto = "devuelto"
    
    estadoChoices = (
        prestado,
        devuelto,
    )
    
    estado = models.Choices(choices = estadoChoices)
    