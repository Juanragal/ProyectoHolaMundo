import datetime as fechas
anho_actual=int(fechas.date.today().year)
nombre_completo=input("Introduce tu nombre completo:")
nombre_incorrecto=len(nombre_completo)<10
while  nombre_incorrecto:
    print("Tu nombre no tiene mas de 10 caracteres")
    print("\n")
    nombre_completo=input("Introduce tu nombre completo:")
    nombre_incorrecto=len(nombre_completo)<10

anho_nacimiento=int(input("Introduce tu año de nacimiento:"))
edad=anho_actual-anho_nacimiento
anho_incorrecto=edad<18
while anho_incorrecto:
    print("No eres mayor de edad")
    print("\n")
    anho_nacimiento=int(input("Introduce tu año de nacimiento:"))
    edad=anho_actual-anho_nacimiento
    anho_incorrecto=edad<18

direccion_email=input("Introduce un correo electrónico:")
email_incorrecto= "@" not in direccion_email
while email_incorrecto:
    print("No has puesto @, vigila el correo")
    print("\n")
    direccion_email=input("Introduce un correo electrónico:")
    email_incorrecto= "@" not in direccion_email

telefono=input("Introduce un telefono:")
telefono_incorrecto= (telefono.isnumeric() == False)
while telefono_incorrecto:
    print("No es un número. Por favor, introduce un número")
    print("\n")
    telefono=input("Introduce un telefono:")
    telefono_incorrecto= (telefono.isnumeric() == False)

print("Felicidades, tu registro es correcto")

