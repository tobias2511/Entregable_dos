from django.contrib import admin
from .models import *
# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','comision')
    search_fields = ('nombre','comision')
    
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email')
    search_fields = ('nombre','apellido','email')

class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email','profesion')
    search_fields = ('nombre','apellido','email','profesion')
    
admin.site.register(Curso,CursoAdmin)
admin.site.register(Estudiantes,EstudiantesAdmin)
admin.site.register(Profesores,ProfesoresAdmin)