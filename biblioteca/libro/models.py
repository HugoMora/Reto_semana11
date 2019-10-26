from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    #autor = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tarifa(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    inicio = models.DateField()
    fin = models.DateField()
    precio_por_dia = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre


class AlquilerDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_alquiler = models.DateField(auto_now_add=True)
    id_alquiler = models.ForeignKey('Alquiler', on_delete=models.CASCADE)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_tarifa = models.ForeignKey('Tarifa', on_delete=models.CASCADE)
    cantidad_dias = models.IntegerField()

class LibroCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
