import json

titulo=input("Introduce titulo de pelicula:")
texto_plano=""
with open(titulo+".json","r") as fichero:
    linea=fichero.readline()
    while linea != "":
        texto_plano+=linea
        linea=fichero.readline()
diccionario=json.loads(texto_plano)

print("El director de {} es {}".format(diccionario["Title"],diccionario["Director"]))
for i in diccionario["Ratings"]:
    print("La fuente {} le ha dado un valor de {}".format(i["Source"],i["Value"]))