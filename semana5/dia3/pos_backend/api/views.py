from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Categoria,Mesa,Plato
)
from .serializers import (
    CategoriaSerializers,
    MesaSerializers,
    PlatoSerializers
)

class IndexView(APIView):

    def get(self,request):
        context = {
            'ok':True,
            'message':'el servidor esta activo!'
        }
        return Response(context)

class CategoriaView(APIView):

    def get(self,request):
        dataCategoria = Categoria.objects.all()
        serCategoria = CategoriaSerializers(dataCategoria,many=True)
        context = {
            'ok' : True,
            'content' : serCategoria.data
        }

        return Response(context)

class MesaView(APIView):

    def get(self,request):
        dataMesa = Mesa.objects.all()
        serMesa = MesaSerializers(dataMesa,many=True)
        context = {
            'ok' : True,
            'content' : serMesa.data
        }

        return Response(context)

class PlatoView(APIView):
    def get(self,request):
        dataPlato = Plato.objects.all()
        serPlato = PlatoSerializers(dataPlato,many=True)
        context = {
            'ok' : True,
            'content' : serPlato.data
        }

        return Response(context)