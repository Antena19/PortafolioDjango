#myportfolio/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactoForm
from .models import Proyecto, Contacto
#AGREGADAS PARA CORREO
from django.core.mail import send_mail
from django.conf import settings

#Vista para la pagina de inicio que muestra los proyectos
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

#Vistas Crud administración de usuarios en el formulario de contacto
def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

#Eliminar
@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'myportfolio/contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

#Listar Contactos
@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'myportfolio/contacto_lista.html', {'contactos': contactos})
#Confirmación
def contacto_confirmacion(request):
    return render(request, 'myportfolio/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')
    