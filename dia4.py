#crear clase
class Automovil:
    #!crear atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.col = col
        self.marca = mar
    #metodos
    def encender(self):
        print("encender: " + self.marca)
    def avanzar(self):
        print("avanzar: " + self.marca)
    def acelerar(self):
        print("acelerar: " + self.marca)
    def frenar(self):
        print("frenar: " + self.marca)
#crer un objeto
vw = Automovil(1970,"VH-159","amarillo","volkswagen")
tico = Automovil(1970,"VH-159","rojo","tico")
#utilizar el objeto
vw.encender()
tico.frenar()