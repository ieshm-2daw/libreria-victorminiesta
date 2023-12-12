from django.urls import path
from .views import ListLibros, DetailLibro, DeleteLibro, CreateLibro, UpdateLibro, PrestarLibro

urlpatterns = [
    path('', ListLibros.as_view(), name='listadoLibros'),
    path('libro/<int:pk>/', DetailLibro.as_view(), name='detalleLibros'),
    path('libro/delete/<int:pk>', DeleteLibro.as_view(), name='deleteLibros'),
    path('libro/new', CreateLibro.as_view(), name='createLibros'),
    path('libro/edit/<int:pk>', UpdateLibro.as_view(), name='updateLibro'),
    path('libro/prestar/<int:pk>', PrestarLibro.as_view(), name='prestarLibro'),
]
