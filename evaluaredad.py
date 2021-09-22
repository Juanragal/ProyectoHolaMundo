import datetime as fechas
anho_nacimiento=int(input("Indica tu año de nacimiento:"))
anho_actual=int(fechas.date.today().year)
edad = anho_actual - anho_nacimiento
if edad < 18:
    print("Uy, si aun no puedes votar! Tienes",edad , "años!")
elif edad < 40:
    print("Vete ya de casa de tus padres y vete buscando independencia enconómica, que ya tienes", edad, "añazos!")
elif edad < 65:
    print("Ya has hecho la declaración de la renta? con los", edad, "años que tienes ya toca aportar al estado!")
else:
    print("A descansar! Que con tus", edad, "años ahora toca disfrutar de la jubilación! Ves mirando los viajes del imserso!")
