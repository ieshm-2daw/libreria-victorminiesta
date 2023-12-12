from datetime import date
from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import prestamoForm


# Create your views here.

class ListLibros(ListView):
    model = Libro
    
   # queryset=Libro.objects.filter(disponibilidad="D")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)   
        
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad="D")
        context['libros_prestados'] = Libro.objects.filter(disponibilidad="P")
        context['libros_reservados'] = Libro.objects.filter(disponibilidad="R")
        
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
        fecha_devolucion = "2023-12-26"
        Prestamo.objects.create(libro_prestado = libro, 
                                fecha_prestamo = fecha_prestamo, 
                                fecha_devolucion = fecha_devolucion,
                                usuario_prestamo = usuario,
                                estado = "P")
        libro.disponibilidad = "P"
        libro.save()
        return redirect('listadoLibros')
    
        
            
            
    
    
