from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from appfront import views as encuesta

def index(request):
    return HttpResponse('<center><h1>HOLA MUNDO EN DJANGO!!!!!</h1></center>')

urlpatterns = [
    path('',index),
    path('encuesta/',include('appfront.urls')),
    path('admin/',admin.site.urls),
]
