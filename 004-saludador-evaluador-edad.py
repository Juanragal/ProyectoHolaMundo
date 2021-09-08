nombre=input("Dime tu nombre:")
edad=input("¿Me puedes decir tu edad?:")
edad=int(edad)
if edad>=18:
    print("¡Hola ",nombre,"!/n Tienes una edad suficiente para conducir!", sep= "")
else:
    print("Hola ",nombre, "... Por muy bien que me caigas no puedo dejarte conducir...", sep= "")