from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField("Categoria", max_length=20)
    def __str__(self):
        return str(self.categoria)
    
class Lector(models.Model):
    nombre= models.CharField("Nombre lector", max_length=20)
    apellidos= models.CharField("Apellido", max_length=20)
    nacionalidad= models.CharField("Nacionalidad", max_length=20)
    edad= models.IntegerField(default=0)
    def __str__(self):
        return str(self.nombre)
    
class Autor(models.Model):
    nombre= models.CharField("Nombre autor", max_length=20)
    apellidos= models.CharField("Apellido", max_length=20)
    nacionalidad= models.CharField("Nacionalidad", max_length=20)
    edad= models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.nombre) + " "+str(self.apellidos) +" "+ str(self.nacionalidad) +" " +str(self.edad)
 
class Libro(models.Model):
    titulo= models.CharField("Titulo", max_length=20)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores=models.ManyToManyField(Autor)
    fechaLanzamiento= models.DateField("Fecha de lanzamiento")
    portada=models.ImageField(upload_to='imagenes/')
    visitas=models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.titulo) + " "+str(self.fechaLanzamiento) +" "+ str(self.portada) +" " +str(self.visitas)

class Prestamo(models.Model):
    lector=models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPrestamo=models.DateField("Fecha del prestamo")
    fechaDevolucion=models.DateField("Fecha de devolucion")
    devuelto=models.BooleanField("Devuelto: ")
    def __str__(self):

        return "Prestado desde " + str(self.fechaPrestamo) + " Hasta "+str(self.fechaDevolucion) +" devuelto "+ str(self.devuelto)
