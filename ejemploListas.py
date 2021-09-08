import urllib.request
import re
webPage = urllib.request.urlopen("https://www.gutenberg.org/files/2000/2000-0.txt")
frase = webPage.read()
frase = str(frase)
frase = frase.upper()
print(type(frase))
cont = re.split(" |,|\\\\N|\\\\R",frase)
#cont = frase.split()
consulta = input("Que palabra quieres buscar en el quijote?:")
consulta = consulta.upper()
if consulta in cont :
    print (consulta, " ha aparecido en la búsqueda",cont.count(consulta),"veces")
else:
    print ("no aparece ",consulta, "en el quijote")