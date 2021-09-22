import winsound

DMS = 15
DS = 15.9
D = 18.4
PS = 24.9
S = 29.9
OM = 34.9
OS = 39.9

peso = float(input("Introduce tu peso en Kg:"))
altura = float(input("Introduce tu altura en m:"))

indice = peso/altura**2

if indice <= DMS:
    estado ="¡MADRE DEL AMOR HERMOSO, COME ALGO POR DIÓS!"
    estado2 = "Delgadez muy severa"
    winsound.Beep(1000,500)
    winsound.Beep(100,500)
    winsound.Beep(1000,500)
    winsound.Beep(100,500)
elif indice <= DS:
    estado = "¿Te hago un caldito?"
    estado2 = "Delgadez Severa"
    winsound.Beep(800,500)
elif indice <= D:
    estado = "¿Cuanto hace que no almuerzas?"
    estado2 = "Delgadez"
    winsound.Beep(600,500)
elif indice <= PS:
    estado = "Se nota el gimnasio, eh...."
    estado2 = "Peso saludable"
    winsound.Beep(400,500)
elif indice <= S:
    estado = "Ese croasant te sobraba y lo sabes"
    estado2 = "Sobrepeso"
    winsound.Beep(600,500)
elif indice <= OM:
    estado = "Oh, oh... ves pensando en comprarte ropa"
    estado2 = "Obesidad Moderada"
    winsound.Beep(800,500)
elif indice <= OS:
    estado = "Te has planteado ensanchar las puertas?"
    estado2 = "Obesidad Severa"
    winsound.Beep(1000,500)
else:
    estado = "Van los reporteros de documentales americanos a grabarte, limpia la casa."
    estado2 = "Obesidad muy severa"
    winsound.Beep(1000,500)
    winsound.Beep(100,500)
    winsound.Beep(1000,500)
    winsound.Beep(100,500)
print("Tu indice de masa corporal es de", ("%.2f" % indice), "tienes", estado2,".",estado)