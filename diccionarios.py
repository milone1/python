#Diccionarios
alumns = {
    "name": "Erick",
    "last_name": "Milan",
    "email": "erickmilan1002@gmail.com",
    "celar": 995560456
}

#Imprime el diccionario completo
print(alumns)

#Como imprimir un valor
print(alumns["celar"])

#Como Ingresar un valor al diccionario
alumns["address"] = "pjs San Carlos"
print(alumns)

#Como actualizar un valor 
alumns["name"] = "Ronal"
print(alumns)

#Como eliminar un key y su valor 
del(alumns["address"])
print(alumns)