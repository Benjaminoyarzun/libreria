from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField("Categoria", max_length=20)
    def __str__(self):
        return self.categoria
    
class Lector(models.Model):
    nombre= models.CharField("Nombre lector", max_length=20)
    apellidos= models.CharField("Apellido", max_length=20)
    nacionalidad= models.CharField("Nacionalidad", max_length=20)
    edad= models.IntegerField(default=0)
    def __str__(self):
        return self.nombre   
class Autor(models.Model):
    nombre= models.CharField("Nombre autor", max_length=20)
    apellidos= models.CharField("Apellido", max_length=20)
    nacionalidad= models.CharField("Nacionalidad", max_length=20)
    edad= models.models.IntegerField(default=0)
    def __str__(self):
        return self.nombre
 
class Libro(models.Model):
    titulo= models.CharField("Titulo", max_length=20)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores=models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_lanzamiento= models.DateField("Fecha de lanzamiento")
    portada=models.ImageField(upload_to='imagenes/')
    visitas=models.IntegerField(default=0)

class Prestamo(models.Model):
    lector=models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo=models.DateField("Fecha del prestamo")
    fecha_devolucion=models.DateField("Fecha de devolucion")
    devuelto=models.DateField("Devuelto el dia")
