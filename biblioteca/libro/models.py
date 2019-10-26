from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    #autor = models.CharField(max_length=100)
    descripcion = models.TextField()

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Alquiler(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)

class Tarifa(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    inicio = models.DateField()
    fin = models.DateField()
    precio_por_dia = models.IntegerField()

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni = models.IntegerField()


class AlquilerDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_alquiler = models.DateField(auto_now_add=True)
    cantidad_dias = models.IntegerField()
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_alquiler = models.ForeignKey('Alquiler', on_delete=models.CASCADE)
    id_tarifa = models.ForeignKey('Tarifa', on_delete=models.CASCADE)

class LibroCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
