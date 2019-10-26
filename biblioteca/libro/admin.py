from django.contrib import admin
from .models import (Libro, Persona, Categoria,
                    Alquiler, Tarifa, AlquilerDetalle,
                    LibroCategoria)

# Register your models here.
admin.site.register(Libro)
admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Alquiler)
admin.site.register(AlquilerDetalle)
admin.site.register(Tarifa)
admin.site.register(LibroCategoria)