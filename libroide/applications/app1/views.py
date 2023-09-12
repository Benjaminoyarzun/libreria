from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Prestamo, Libro
from .forms import PrestamoForm, LibroForm

class Prestamo(ListView):
    template_name ="librovich.html"
    model=Prestamo
    context_object_name="prestamo"
    

def prestamoForm(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaPrestamo')  # Redireccionar a la lista después de guardar
    else:
        form = PrestamoForm()
    return render(request, 'index.html', {'form': form})

class Libro(ListView):
    template_name ="librovich.html"
    model=Libro
    context_object_name="libro"

def libroForm(request):
    if request.method == 'POST':
        form2 = LibroForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('listaLibro')  # Redireccionar a la lista después de guardar
    else:
        form2 = LibroForm()
    return render(request, 'index.html', {'form2': form2})