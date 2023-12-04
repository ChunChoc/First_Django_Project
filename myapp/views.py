from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Medico, Paciente

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'right-sidebar.html')

def select(request):
    return render(request, 'buttons.html')

def patient(request):
    return render(request, 'patient.html')

def doctor(request):
    return render(request, 'doctor.html')


@csrf_exempt
def doctor(request):
    if request.method == "POST":
        # Obtener datos del formulario
        nombre_medico = request.POST.get('nombre_medico')
        numero_colegiado = request.POST.get('numero_colegiado')
        especialidad = request.POST.get('especialidad')
        diagnostico = request.POST.get('diagnostico')
        
        # Crear instancia del modelo Medico y guardar en base de datos
        medico = Medico(
            nombre=nombre_medico,
            numero_colegiado=numero_colegiado,
            especialidad=especialidad,
            diagnostico=diagnostico
        )
        medico.save()

        # Redirigir a alguna página de éxito o de vuelta al formulario
        return redirect('home')  # Cambia 'home' por el nombre de la URL a la que deseas redirigir

    # Si no es una solicitud POST, simplemente renderiza el formulario
    return render(request, 'doctor.html')


@csrf_exempt
def patient(request):
    if request.method == "POST":
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        dpi = request.POST.get('dpi')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        direccion = request.POST.get('direccion')
        razon_visita = request.POST.get('razon_visita')
        receta_medica = request.POST.get('receta_medica', '')  # Este campo es opcional
        numero_telefonico = request.POST.get('numero_telefonico')
        
        # Crear instancia del modelo Paciente y guardar en base de datos
        paciente = Paciente(
            nombre=nombre,
            dpi=dpi,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            razon_visita=razon_visita,
            receta_medica=receta_medica,
            numero_telefonico=numero_telefonico
        )
        paciente.save()

        # Redirigir a alguna página de éxito o de vuelta al formulario
        return redirect('home')  # Cambia 'home' por el nombre de la URL a la que deseas redirigir

    # Si no es una solicitud POST, simplemente renderiza el formulario
    return render(request, 'patient.html')