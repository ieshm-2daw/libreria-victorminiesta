from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='fotoAutores/')
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    sitioWeb = models.URLField()
    
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    resume = models.TextField()
    
    DISPONIBILIDAD_CHOICES=(
        ('D','Disponible'),
        ('P','Prestado'),
        ('R','Reservado'),
    )
    disponibilidad=models.CharField(max_length=50, choices=DISPONIBILIDAD_CHOICES)
    portada = models.ImageField(upload_to='portadas/')
    
    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    usuario_prestamo = models.CharField(max_length=100)
    
    ESTADO_CHOICES=(
        ('D','Devuelto'),
        ('P','Prestado'),
    )
    estado=models.CharField(max_length=50, choices=ESTADO_CHOICES)
    
    def __str__(self):
        return self.libro_prestado
    
class Usuario (AbstractUser):
    dni = models.CharField( max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(9)],null=True)