from rest_framework import serializers
from .models import (
    Mesa,Categoria,Plato
)

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MesaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PlatoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Plato
        fields = '__all__'
        
