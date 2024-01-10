from datetime import date, timedelta
from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import prestamoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#En el caso de tener las vistas basadas en funciones usariamos:
# @login_required

class ListLibros(LoginRequiredMixin,  ListView):
    model = Libro
    template_name = "appBiblioteca/libro_listado.html"
    paginate_by = 2
    
   # queryset=Libro.objects.filter(disponibilidad="D")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['libros'] = Libro.objects.all()
        
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad="Disponible")
        context['libros_prestados'] = Libro.objects.filter(disponibilidad="Prestado")
        context['libros_reservados'] = Libro.objects.filter(disponibilidad="Reservado")
        
        return context
    
class librosDisponible(LoginRequiredMixin, ListView):
    model= Libro
    template_name="appBiblioteca/librosDisponibles.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad = "Disponible")
        
        return context
    
class MisLibros(LoginRequiredMixin, ListView):
    model= Prestamo
    template_name="appBiblioteca/MisLibros.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['Libros_Prestados'] = Prestamo.objects.filter(estado = "Prestado", usuario_prestamo = self.request.user)
        context['Libros_Devueltos'] = Prestamo.objects.filter(estado = "Disponible", usuario_prestamo = self.request.user)
        
        return context
    
class LibrosPrestados(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = "appBiblioteca/librosPrestados.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context['Libros_Prestados'] = Prestamo.objects.filter(estado = "Prestado").order_by('fecha_devolucion')
        context['hoy'] = date.today()
        
        return context
    
class DetailLibro(LoginRequiredMixin, DetailView):
    model = Libro

class DeleteLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('listadoLibros')
    
class CreateLibro(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad','portada']
    success_url = reverse_lazy('listadoLibros')
    '''template_name = "appBiblioteca/libro_form.html" '''
    
class UpdateLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad','portada']
    success_url = reverse_lazy('listadoLibros')
    '''template_name = "appBiblioteca/libro_update_form.html"'''
    
class PrestarLibro(LoginRequiredMixin, View):
    template_name = "appBiblioteca/libro_Prestar.html"
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, self.template_name, {'libro':libro})
    def post(self,request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        usuario = request.user
        fecha_prestamo = date.today()
        fecha_devolucion = fecha_prestamo + timedelta(days=15)
        Prestamo.objects.create(libro_prestado = libro, 
                                fecha_prestamo = fecha_prestamo, 
                                fecha_devolucion = fecha_devolucion,
                                usuario_prestamo = usuario,
                                estado = "Prestado")
        libro.disponibilidad = "Prestado"
        libro.save()
        return redirect('listadoLibros')

class DevolverLibro(LoginRequiredMixin, View):
    template_name = "appBiblioteca/libro_Devolver.html"
    def get(self, request, pk):
        libro_prestado = get_object_or_404(Libro, pk=pk, disponibilidad = 'Prestado')
        return render(request, self.template_name, {'libro': libro_prestado})
    def post(self, request, pk):
        libro_prestado = get_object_or_404(Libro, pk=pk, disponibilidad = 'Prestado')
        prestamo = Prestamo.objects.filter(libro_prestado = libro_prestado, usuario_prestamo = request.user, estado = "Prestado").first()
        prestamo.estado = "Disponible"
        prestamo.fecha_devolucion = date.today()
        prestamo.save()
        
        libro_prestado.disponibilidad = "Disponible"
        libro_prestado.save()
        
        return redirect('listadoLibros')
    
class BuscarLibro(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "appBiblioteca/libro_buscar.html"
    
    # Se utiliza *args para recoger cualquier número de argumentos posicionales que podrían ser pasados a la función 
    # Se utiliza **Kwargs para recoger cualquier número de argumentos de palabras clave que podrían ser pasados a la función
    def get(self, *args, **kwargs):
        titulo = self.request.GET.get("titulo")
        libros = Libro.objects.filter(titulo__icontains=titulo)
        context = {"libros": libros}
        return render(self.request, self.template_name, context)
        
            
            
    
    
