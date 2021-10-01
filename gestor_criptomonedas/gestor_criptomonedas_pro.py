def listToString(s): 
    str1 = "" 
    for i in s: 
        str1 = str1 + i[1] + " "  
    return str1 
NOMBRE_FICHERO="cotizacion.dat"       
def listcotizaciones(nombre_fichero):
    with open(nombre_fichero,"r") as fichero:
        cripto=fichero.readline().replace("\n","")
        listacripto=[]
        while cripto!="":
            acro=fichero.readline().replace("\n","")
            cotizacion=str(fichero.readline()).replace("\n","")
            listacripto.append((cripto,acro,cotizacion))
            cripto=fichero.readline().replace("\n","")
        return listacripto
listacripto=listcotizaciones(NOMBRE_FICHERO)
fichero=open("ordenes_venta_negativo.txt","w")
fichero2=open("ordenes_venta_positivo.txt","w")
for i in listacripto:
    if float(i[2])<0:
        fichero.write("Vende "+i[0]+" cagando leches que está a "+i[2]+" "+i[1])
        fichero.write("\n")
    else:
        fichero2.write("Vende "+i[0]+" cagando leches que está a "+i[2]+" "+i[1])
        fichero2.write("\n")
fichero.close()
fichero2.close()
criptos=[]
for i in listacripto:
    criptos.append(i[1])
criptoduda=input("Que cripto moneda quieres consultar?(" + listToString(listacripto)+"):").upper()
if criptoduda in criptos:
    for i in listacripto:
        if i[1]==criptoduda:
            print(i[0]+" está cotizando a "+i[2]+", tu verás que haces...")
else:
    print("Esa cripto ya ni existe...")