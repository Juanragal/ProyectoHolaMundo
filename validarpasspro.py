import hashlib
from os import read
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()

with open("G:\\Unidades compartidas\\DLN OTE\\MACROTEMP\\Python\\_IntensivoPython\\ProyectoHolaMundo\\5_hash.txt") as f:
    read_data = f.readlines()
clear_data = []
for x in read_data:
    clear_data.append(x.replace("\n", ""))

pwd = input("Introduce tu contraseña:")
print(clear_data)
print(obtener_hash(pwd))
while obtener_hash(pwd) in clear_data:
    print("La contraseña", pwd, "está en uso")
else:
    print("La contraseña es valida")
