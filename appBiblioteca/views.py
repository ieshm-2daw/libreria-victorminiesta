from django.shortcuts import render
from .models import Libro
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class ListLibros(ListView):
    model = Libro
    queryset=Libro.objects.filter(disponibilidad="D")
    
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