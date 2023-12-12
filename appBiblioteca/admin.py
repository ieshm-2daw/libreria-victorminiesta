from django.contrib import admin
from .models import Libro, Usuario, Prestamo
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Usuario, UserAdmin)
admin.site.register(Libro)
admin.site.register(Prestamo)