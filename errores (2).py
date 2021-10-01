class NombreCortoError(Exception):
    def __init__(self):
        self.mensaje="No cuela, tu nombre no puede tener solo dos letras..."
        super().__init__(self.mensaje)
    def solucionar(self):
        print("Solucionando...")

class EdadInsuficienteError(Exception):
    def __init__(self):
        self.mensaje="Tienes que ser mayor de 18..."
        super().__init__(self.mensaje)
    def solucionar(self):
        print("Solucionando...")

class MalGustoError(Exception):
    def __init__(self):
        self.mensaje="En serio Naranja? no te da verguenza?"
        super().__init__(self.mensaje)
    def solucionar(self):
        print("Solucionando...")

def testcolor(color):
    if color=="Naranja":
        raise MalGustoError()
    return color

def testedad(edad):
    if edad < 18:
        raise EdadInsuficienteError()
    return edad

def testnombre(nombre):
    if len(nombre)<3:
        raise NombreCortoError()
    return nombre



nombre=input("Introduzca su nombre:")
edad=int(input("Introduzca su edad:"))
color=input("Introduce tu color favorito:")
print(testnombre(nombre))
print(testedad(edad))
print(testcolor(color))

