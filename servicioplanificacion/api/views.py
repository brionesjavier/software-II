from django.shortcuts import render

from rest_framework import generics
from .serializers import CursoSerializer
from .models import Curso

class CreateView(generics.ListCreateAPIView):
    """Vista que representa el comportamiento de la API REST."""
    #El queryset contiene la colección dcon todos los cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def perform_create(self, serializer):
        """Almacena los datos recibidos mediante POST como un Curso."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Vista que maneja las peticiones GET; PUT y DELETE."""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
