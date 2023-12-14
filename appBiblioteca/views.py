from datetime import date, timedelta
from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import prestamoForm
from django.contrib.auth.models import User


# Create your views here.

class ListLibros(ListView):
    model = Libro
    template_name = "appBiblioteca/libro_listado.html"
    
   # queryset=Libro.objects.filter(disponibilidad="D")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['libros'] = Libro.objects.all()
        
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad="Disponible")
        context['libros_prestados'] = Libro.objects.filter(disponibilidad="Prestado")
        context['libros_reservados'] = Libro.objects.filter(disponibilidad="Reservado")
        
        return context
    
class librosDisponible(ListView):
    model= Libro
    template_name="appBiblioteca/librosDisponibles.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad = "Disponible")
        
        return context
    
class MisLibros(ListView):
    model= Prestamo
    template_name="appBiblioteca/MisLibros.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['Libros_Prestados'] = Prestamo.objects.filter(estado = "Prestado", usuario_prestamo = self.request.user)
        context['Libros_Devueltos'] = Prestamo.objects.filter(estado = "Disponible", usuario_prestamo = self.request.user)
        
        return context
    
class LibrosPrestados(ListView):
    model = Prestamo
    template_name = "appBiblioteca/librosPrestados.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context['Libros_Prestados'] = Prestamo.objects.filter(estado = "Prestado").order_by('fecha_devolucion')
        context['hoy'] = date.today()
        
        return context
    
class DetailLibro(DetailView):
    model = Libro

class DeleteLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('listadoLibros')
    
class CreateLibro(CreateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad','portada']
    success_url = reverse_lazy('listadoLibros')
    '''template_name = "appBiblioteca/libro_form.html" '''
    
class UpdateLibro(UpdateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad','portada']
    success_url = reverse_lazy('listadoLibros')
    '''template_name = "appBiblioteca/libro_update_form.html"'''
    
class PrestarLibro(View):
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

class DevolverLibro(View):
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
        
            
            
    
    
