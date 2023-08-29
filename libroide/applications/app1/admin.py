from django.contrib import admin
from .models import Prestamo, Libro, Autor, Lector, Categoria
# Register your models here.
admin.site.register(Prestamo)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Lector)
admin.site.register(Categoria)
