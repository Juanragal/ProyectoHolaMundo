import winsound
EXTENSION = ".txt"

DMS = 15
DS = 15.9
D = 18.4
PS = 24.9
S = 29.9
OM = 34.9
OS = 39.9

peso = float(input("Introduce tu peso en Kg:"))
altura = float(input("Introduce tu altura en m:"))
nombre = input("Introduce tu nombre:")
indice = peso/altura**2

if indice <= DMS:
    estado ="¡MADRE DEL AMOR HERMOSO, COME ALGO POR DIÓS!"
    estado2 = "Delgadez muy severa"
elif indice <= DS:
    estado = "¿Te hago un caldito?"
    estado2 = "Delgadez Severa"
elif indice <= D:
    estado = "¿Cuanto hace que no almuerzas?"
    estado2 = "Delgadez"
elif indice <= PS:
    estado = "Se nota el gimnasio, eh...."
    estado2 = "Peso saludable"
elif indice <= S:
    estado = "Ese croasant te sobraba y lo sabes"
    estado2 = "Sobrepeso"
elif indice <= OM:
    estado = "Oh, oh... ves pensando en comprarte ropa"
    estado2 = "Obesidad Moderada"
elif indice <= OS:
    estado = "Te has planteado ensanchar las puertas?"
    estado2 = "Obesidad Severa"
else:
    estado = "Van los reporteros de documentales americanos a grabarte, limpia la casa."
    estado2 = "Obesidad muy severa"
nombre_fichero = nombre.replace(" ","_").lower() + EXTENSION
fichero = open(nombre_fichero, "w")
fichero.write("Hola " + nombre + ". Tu indice de masa corporal es de " + str(round(indice,2)))
fichero.write("\n")
fichero.write("tienes " + estado2)
fichero.write("\n")
fichero.write(estado) 
