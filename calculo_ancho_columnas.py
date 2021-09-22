

def calcular_ancho_columna(lista):
    long=0
    for y,k in lista.items():
        if len(str(y))>long:
            long=len(str(y))
        for i in k:
            if len(str(i))>long:
                long=len(str(i))
    return long
    
texto={122121212222222121223:("kkakaksssssskk",2323232),4:(2500,26)}
print(calcular_ancho_columna(texto))