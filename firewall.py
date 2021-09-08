INTENTOS=3
SWITCHOFF="0"
ip="-1"
listaip=[]
blacklist=[]
while ip!=SWITCHOFF:
    ip=input("Introcude una dirección IP:")
    #if (listaip.count(ip)<2) or (ip not in blacklist):
    if ip not in blacklist:
        listaip.append(ip)
        if listaip.count(ip)==INTENTOS:
            blacklist.append(ip)
    else: 
        print("Tu ip se ha encontrado en una lista negra... ")
print(listaip)
