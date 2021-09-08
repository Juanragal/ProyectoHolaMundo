MAYORIA_EDAD = 18
print("Necesitamos tener datos tuyos para saber si te contratamos")
edad = int(input("indica tu edad:"))
nacionalidad = input ("indica tu nacionalidad:")
idioma1 = input("indica tu primer idioma extranjero:")
idioma2 = input("indica tu segundo idioma extranjero")
mayor_edad = edad>=MAYORIA_EDAD
nacionalidad_ok = (nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad!="Ruso"
idiomas_ok = idioma1=="Ingles" and idioma2=="Chino"

if (mayor_edad and nacionalidad_ok and idiomas_ok):
    print("Contratado")
else  :
    print("no cumples el perfil")