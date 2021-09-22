numeros=[3,8,10,23,0]
n1=input("Introduce el primer indice del rango deseado, recuerda que debe ser entre el 0 y el 4:")
n2=input("Introduce el segundo indice del rango deseado, recuerda que debe ser entre el 0 y el 4:")
try:
    numero=numeros[int(n1)]/numeros[int(n2)]
    
except ValueError:
    print("No has puesto un número, sabes donde están en el teclado?")
except IndexError:
    print("Que no has entendido entre 0 y 4?")
except ZeroDivisionError:
    print("Ups, pues parece que estamos dividiendo por 0")
except:
    print("Yo ya no se que leches has hecho, pero esto no funciona... búscate otro ordenador que te aguante")
else:
    print("El resultado es",numero)