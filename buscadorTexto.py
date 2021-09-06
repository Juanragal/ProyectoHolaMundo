import urllib.request
webPage = urllib.request.urlopen("https://www.as.com")
frase = webPage.read()
print(frase)

frase="EN UN LUGAR DE LA MANCHA, LA MANCHA ES UNA REGION"
consulta = input("Elemento a buscar;")
ocurrencias = frase.count(consulta.upper())
print("El texto buscado ha aparecido", ocurrencias,"veces")