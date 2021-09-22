DIASTOLICA_LIMITE = 84
SISTOLICA_LIMITE = 129

diastolica = int(input("Introduce la presión baja (diastolica):"))
sistolica = int(input("Introduce la presion alta (sistolica)"))
if diastolica<=DIASTOLICA_LIMITE and sistolica<=SISTOLICA_LIMITE:
    estado="NORMAL"
else:
    estado="APRENSIVO"
print("El estado de la tensión es", estado)