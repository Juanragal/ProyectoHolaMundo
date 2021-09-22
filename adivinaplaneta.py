import random
planetas =["Mercurio","Marte","Venus","Jupiter","Saturno","Urano","Neptuno","Pluton"]
planetascaps = []
for planeta in planetas:
    planetascaps.append(planeta.upper())
planeta_secreto=random.choice(planetas).upper()
planeta_usuario=input("Introduce el planeta del sistema solar secreto:").upper()

while planeta_usuario!=planeta_secreto:
    planetascaps.remove(planeta_usuario)
    planeta_usuario=input("error!! El planeta elegido no es el correcto. tienes "+ str(len(planetascaps)) + " oportunidades de acertar. Prueba de nuevo"+ str(planetascaps) ).upper()
else:
    print("Felicidades! Justo estabamos pensando en",planeta_usuario )