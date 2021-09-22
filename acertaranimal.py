animales =["Dog","Cat","Bird","Cow","Snake"]
animalescap=[]
for animal in animales:
    animalescap.append(animal.upper())
ani=input("Introduce un nombre de animal en inglés:").upper()
while ani not in animalescap:
    ani=input("Introduce un nombre de animal en inglés:").upper()
print("Correcto")