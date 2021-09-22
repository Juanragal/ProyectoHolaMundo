lista_nombres = [["Fernando", 1971], ["Francisco", 1988], ["Javier", 1990], ["Jose", 1973], ["Federica", 1999]]
print(lista_nombres[1])
inicial = input("Introduce la inicial del nombre que buscas:").upper
anho = int(input("Introduce el año:"))
lista_resultado = []
for item in lista_nombres:
    x=item[0].startswith(inicial)
    print(x) #and anho > item[1]: 
     #   lista_resultado.append(item[0])
#print(lista_resultado)