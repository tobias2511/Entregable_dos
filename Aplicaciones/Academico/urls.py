from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio,name="inicio"),
    
    path('cursos/',cursos,name="cursos"),
    path('estudiantes/',estudiantes,name="estudiantes"),
    path('profesores/',profesores,name="profesores"),
    path('base/',base,name="base"),
    path('registrarCurso/',registrarCurso),
    path('registrarEstudiante/',registrarEstudiante),
    path('registrarProfesor/',registrarProfesor),
    
]
