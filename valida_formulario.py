import datetime as fechas
anho_actual=int(fechas.date.today().year)
Nombre_completo=input("Introduce tu nombre completo:")
Anho_nacimiento=int(input("Introduce tu año de nacimiento:"))
Direccion_email=input("Introduce un correo electrónico:")
Telefono=input("Introduce un telefono:")
nombre_correcto=len(Nombre_completo)>=10
edad=anho_actual-Anho_nacimiento
anho_correcto=edad>=18
email_correcto= "@" in Direccion_email
telefono_correcto= Telefono.isnumeric()
if nombre_correcto:
    if anho_correcto:
        if email_correcto:
            if telefono_correcto:
                estado = "Correcto"
            else:
                estado = "Telefono no es numérico"
        else:
            estado = "el correo no contiene @"
    else:
        estado="No eres mayor de edad"
else:
    estado="El nombre no supera 10 caracteres"
print(estado)

