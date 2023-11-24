from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


# Create your models here.

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    sitioWeb = models.URLField()
    
    def _str_(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=80)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    ISBN = models.BigIntegerField()
    resumen = models.TextField()

    disponibilidad_choices = (
        ("disponible","Disponible"),
        ("reservado", "Reservado"),
        ("prestamo","Prestamo"),
    )
    disponibilidad = models.CharField(max_length=20, choices=disponibilidad_choices, default="disponible")
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    
    def _str_(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    biografia = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    
    def _str_(self):
        return self.nombre

class Prestamo(models.Model):
    libroPrestado = models.CharField(max_length=50)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField()
    usuario = models.CharField(max_length=50)
    
    estado_choices = (
        ("prestado","Prestado"),
        ("devuelto","Devuelto"),
    )
    
    estado = models.CharField(max_length=20, choices=estado_choices, default="prestado")
    
    def _str_(self):
        return self.libroPrestado


'''
@login_required
'''
    