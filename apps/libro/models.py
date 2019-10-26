from django.db import models


class libro(models.Model):
    titulo = models.CharField(max_length=200)
    #autor = models.CharField(max_length=100)
    descripcion = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Alquiler(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Tarifa(models.Model):
    descripcion = models.TextField()
    inicio = models.DateField()
    fin = models.DateField()
    precio_por_dia = models.IntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=8)






class Alquiler(models.Model):
    fecha_alquiler = models.DateTimeField(auto_now_add=True)
