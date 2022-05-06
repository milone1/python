from configparser import DuplicateSectionError
import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
print("-" * 50)
print("|" + " " * 9 + "         STORE       " + " "* 18 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES:    " + " "* 18 + "|")
print("|" + " " * 9 + "[1] AGREGAR PRODUCTO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] ELIMINAR PRODUCTO" + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR PRODUCTO" + " "* 16 + "|")
print("|" + " " * 9 + "[4] ELIMINAR PRODUCTO" + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)
opcion = 0
productos = {1:'Pantalon', 2:'Camisas',3:'Corbatas',4:'Casacas'}
precios = {1: "200.00", 2: "120.00", 3: "50.00", 4: "350.00"}
stock = {1: "50", 2: "45", 3: "30", 4: "15"}

while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO PRODUCTO")
        nombre  = input("NOMBRE  : ")
        precio = input("PRECIO   : ")
        acumulado = input("STOCK : ")

        dictProductos= {
            'id': id,
            'nombre':nombre
        }
        dictPrecios = {
            'id': id,
            'precio': precio
        }
        dictAcumulados = {
            'id': id,
            'stock': acumulado 
        }
        productos.append(dictProductos)
        precios.append(dictPrecios)
        stock.append(dictAcumulados)

        print("PRODUCTO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE PRODUCTOS")
        cabeceras = productos[0].keys()
        registros = [x.values() for x in productos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")