#Tabla de multiplicar 

cadena = input("Cadena de: ")
lado = int(input("Ingrese el numero de lado:"))

for i in range(1,lado + 1, 1):
    if( i == 1 or i == lado):
        print((cadena + " ") * lado)
    else:
        print((cadena+" ") + "  " * (lado - 2) + cadena)