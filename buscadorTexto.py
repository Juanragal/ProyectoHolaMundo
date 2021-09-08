import urllib.request
from win10toast import ToastNotifier
webPage = urllib.request.urlopen("https://www.as.com")
frase = webPage.read()
frase = str(frase)
print(type(frase))
veces = frase.count("baloncesto")
texto = ("se han encontrado" + str(veces) + " la palabra baloncesto en la web del AS")
toaster = ToastNotifier()
toaster.show_toast("juanra aviso", texto)
#frase="EN UN LUGAR DE LA MANCHA, LA MANCHA ES UNA REGION"
#consulta = input("Elemento a buscar;")
#ocurrencias = frase.count(consulta.upper())
#print("El texto buscado ha aparecido", ocurrencias,"veces")