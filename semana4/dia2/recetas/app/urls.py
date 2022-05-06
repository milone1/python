from django.urls import URLPattern, path

from . import views

app_name = 'app'

urlpatterns = [
    ##las comillas vacias representan el home de la pagina o ruta principal
    ##entra al archivo views que esta dentro de la carpeta app y despues llama a a la funcion index que resive por parametro el request.
    # el namo que esta ahi es como un alias 
    path('',views.index,name='index'),

    path('registrarReceta',views.registrarReceta,name='registrarReceta')
]