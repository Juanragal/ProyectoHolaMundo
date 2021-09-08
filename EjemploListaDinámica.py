numeros_pares = []
a=1
n=int(input("Introduce el número final de tu lista:"))
while a <= n:
    if a % 2 == 0:
        numeros_pares.append(a)
        a+=1
    else:
        a+=1
print(numeros_pares) 