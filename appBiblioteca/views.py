from django.shortcuts import render
from .models import Libro
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class ListLibros(ListView):
    model = Libro
    
class DetailLibro(DetailView):
    model = Libro

class DeleteLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('listadoLibros')
    
class CreateLibro(CreateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad']
    success_url = reverse_lazy('listadoLibros')
    
class UpdateLibro(UpdateView):
    model = Libro
    fields = ['titulo','autor', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resume', 'disponibilidad']
    success_url = reverse_lazy('listadoLibros')