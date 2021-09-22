import random
vocales=["a","e","i","o","u","y","ä","å","ö","ü"]
vocalestilde=["ä","å","ö","ü"]
consonantes=["š","ž","b","c","d","f","j","k","g","h","l","m","n","p","q","r","s","t","v","z","w","x"]
letras=vocales+consonantes
letras.sort()
furnitures=["Mesa comedor","Canapé","Silla","Comoda","Mesita de noche","Mueble baño","Tocador"]
def haytresconsonante(nombre):
    if nombre[0] in consonantes and nombre[1] in consonantes and nombre[2]in consonantes:
        return True
def haytrevocales(nombre):
    if nombre[0] in vocales and nombre[1] in vocales and nombre[2] in vocales:
        return True
def dostildes(nombre):
    nom=list(nombre.split())
    if len(nom.intersection(vocalestilde))>2:
        return True
def naming(opcion):
    n=0
    name=random.choice(letras)
    while n!=opcion:
        if  len(name)<3:
            name = random.choice(letras)+name
            n+=1
        elif haytresconsonante(name):
            name = random.choice(vocales)+name
            n+=1
        elif dostildes(name):
            name = str(random.choice(vocales))+name
            n+=1
        elif haytrevocales(name):
            name = random.choice(consonantes)+name
            n+=1
        else:
            name = random.choice(letras)+name
            n+=1
    name=name[::-1]
    return name.capitalize()
nom_compuesto=random.choice(range(1,3))
x=0
nombrefinal=random.choice(furnitures)
while x!=nom_compuesto:
    nombrefinal=nombrefinal+" "+naming(random.choice(range(3,9)))
    x+=1
print(nombrefinal)

