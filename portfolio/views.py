from django.core.mail import send_mail
from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.contrib import messages

def landing(request):
    return render(request, 'portfolio/landing.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']

            asunto = f"Nuevo mensaje de contacto de {nombre}"
            cuerpo = f"De: {nombre} <{correo}>\n\nMensaje:\n{mensaje}"

            send_mail(asunto, cuerpo, correo, ['mmalexis9@gmail.com'])  # <-- tu correo destino

            messages.success(request, '¡Mensaje enviado correctamente!')
            form = ContactForm()  # limpia el formulario
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})