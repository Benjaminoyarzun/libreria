from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Prestamo
from .forms import PrestamoForm

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

