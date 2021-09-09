vehiculo1 = ["Skoda", "Kodiak", "blanco"]
vehiculo2 = ["Opel", "Corsa", "negro"]
vehiculo3 = ["Seat", "tarraco","azul"]
diccionario = {"4356 LGT": vehiculo1,"2563 DLN": vehiculo2,"5555 BCN": vehiculo3}
matricula = input("introduce la matricula:")
#if matricula in diccionario:
#    print(diccionario.get(matricula))
#else:
#    print("Esa matricula no existe!")

try:
    vehiculo = diccionario[matricula]
    print(vehiculo)
except:
    print("Que dimiti ni dimiti de que!")