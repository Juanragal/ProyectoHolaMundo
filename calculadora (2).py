def sumar(n1,n2):
    resultado=n1+n2
    return resultado

def restar(n1,n2):
    resultado=n1-n2
    return resultado

def multiplicar(n1,n2):
    resultado=n1*n2
    return resultado

def dividir(n1,n2):
    resultado=n1/n2
    return resultado

def salir():
    return False


opciones = {1:"sumar",2:"restar",3:"multiplicar",4:"dividir",0:"salir"}
for x in opciones:
    print(str(x) + "-" + str(opciones[x]))
try:
    operacion=int(input("Introduce la operación que quieres hacer"))
    while  operacion!=0:
        n1 = float(input("indica el valor del primer operando:"))
        n2 = float(input("indica el valor del segundo operando:"))
        final = eval(opciones[operacion]+"("+str(n1) +","+str(n2)+")")
        print("el resultado de",opciones[operacion], str(n1), "y", str(n2), "es", str(final))
        for x in opciones:
            print(str(x) + "-" + opciones[x])
        operacion=int(input("Que otra operación quieres hacer?"))
    else:
        print("Gracias por utilizar nuestros servicios!")
except ValueError:
        print("No es numérico")
except ZeroDivisionError:
        print("No se puede dividir por 0")
except:
        print("error desconocido")
