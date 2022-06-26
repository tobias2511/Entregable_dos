from sys import maxsize
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)

class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    profesion = models.CharField(max_length=20)
  