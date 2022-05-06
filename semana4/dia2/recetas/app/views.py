from django.shortcuts import render,redirect

from .models import Receta
from .forms import RecetaForm


# Create your views here.
def index(request):
    ## la funcion index pide renderizar el index.html
    listaRecetas = Receta.objects.all()
    print(listaRecetas)
    ## formulario de recetas:
    frmReceta = RecetaForm()

    context = {
        'frmReceta': frmReceta,
        'recetas': listaRecetas
    }
    return render(request,'index.html',context)

def registrarReceta(request):
    frmReceta = RecetaForm(request.POST)
    if frmReceta.is_valid():
        dataReceta = frmReceta.cleaned_data
        print(dataReceta)
        # insertamos la receta en la tabla 
        nuevaReceta = Receta()
        nuevaReceta.titulo = dataReceta['titulo']
        nuevaReceta.ingredientes = dataReceta['ingredientes']
        nuevaReceta.preparation = dataReceta['preparation']
        nuevaReceta.autor = dataReceta['autor']
        nuevaReceta.save()
    
    return redirect('/')