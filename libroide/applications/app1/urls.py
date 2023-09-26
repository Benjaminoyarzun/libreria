from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('prestamo/', views.Prestamo.as_view(), name='Prestamo'),
    path('index/', views.prestamoForm, name='listaPrestamo'),
]
