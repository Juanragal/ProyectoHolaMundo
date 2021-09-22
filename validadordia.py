dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
dia = input("introduce un dia de la semana:")
for i in dias:
    if i == dia:
        break
    print(i, "no es")
print("Es el", i.capitalize())
