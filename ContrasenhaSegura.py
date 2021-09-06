PALABRA_PROHIBIDA1 = "ADMIN"
PALABRA_PROHIBIDA2 = "123"
PALABRA_PROHIBIDA3 = "PASSWORD"
idUsuario = input("introduzca su identificador:")
contras = input("introduzca su contrasenya: ")
contra = contras.upper()
if contra.find(PALABRA_PROHIBIDA1) < 0:
    if contra.find(PALABRA_PROHIBIDA2) < 0:
        if contra.find(PALABRA_PROHIBIDA3) <0:
            print("Contraseña aceptada")
        else:
            print("No sea usted cenutrio y cúrrese la contraseña si es que te gusta tu privacidad!")
    else:
        print("No sea usted cenutrio y cúrrese la contraseña si es que te gusta tu privacidad!")
else:
    print("No sea usted cenutrio y cúrrese la contraseña si es que te gusta tu privacidad!")
