from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def inicio(request):
    return render(request,"inicio.html",{})

def estudiantes(request):
    estudiantes= Estudiantes.objects.all()
    return render(request,"estudiantes.html",{"estudiantes":estudiantes})

def cursos(request):
    cursos= Curso.objects.all()
    return render(request,"cursos.html",{"cursos":cursos})

def profesores(request):
    profesores= Profesores.objects.all()
    return render(request,"profesores.html",{"profesores":profesores})

def base(request):
    return render(request,"base.html",{})

def registrarCurso(request):
    if request.method == "POST":
        
        info_formulario = request.POST
        
        curso = Curso(nombre = info_formulario['txtNombre'],comision=int(info_formulario['numComision']))
        curso.save()
        return redirect('cursos')
    
def registrarEstudiante(request):
    if request.method == "POST":
        
        info_formulario = request.POST
        
        estudiante = Estudiantes(nombre = info_formulario['txtNombre'],apellido = info_formulario['txtApellido'],email = info_formulario['txtEmail'])
        estudiante.save()
        return redirect('estudiantes')

def registrarProfesor(request):
    if request.method == "POST":
        
        info_formulario = request.POST
        
        profesores = Profesores(nombre = info_formulario['txtNombre'],apellido = info_formulario['txtApellido'],email = info_formulario['txtEmail'],profesion = info_formulario['txtProfesion'])
        profesores.save()
        return redirect('profesores')

