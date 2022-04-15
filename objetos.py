#crear la clase
class Alumno:
    def __init__(self,nombre,edad,email):
        self.name = nombre
        self.age = edad
        self.email = email
    #Crear sus metodos
    def primero(self):
        print("nombre: " + self.name)
        print("edad: " + str(self.age))
        print("email: " + self.email)
    
#crear objeto
nombre = input("Ingrese Nombre:")
edad = input("Ingrese Edad")
email = input("Ingrese Email")
#Utilizar el objeto
colegial = Alumno(nombre,edad,email)

colegial.primero()