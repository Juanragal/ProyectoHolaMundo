with open("cotizacion.dat","r") as fichero:
    cripto=fichero.readline().replace("\n","")
    listacripto=[]
    while cripto!="":
        acro=fichero.readline().replace("\n","")
        cotizacion=str(fichero.readline()).replace("\n","")
        listacripto.append((cripto,acro,cotizacion))
        cripto=fichero.readline().replace("\n","")
    for i in listacripto:
        if float(i[2])<0:
            print("Vende",i[0],"cagando leches que está a",i[2],i[1])
