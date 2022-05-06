from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_index(request):
    titulo = "Encuesta a Alumnos: "
    context = {
        'titulo': titulo
    }

    return render(request,'index.html',context)

def detalle(request,pregunta_id):
    return HttpResponse('pregunta nro %s.' % pregunta_id)

def enviar(request):
    context = {
        'titulo':'resultado de la encuesta:',
        'nombre': request.POST['nombre'],
        'rol': request.POST['rol'],
        'idiomas': request.POST.getlist('idiomas')
    }

    return render(request,'respuesta.html',context)