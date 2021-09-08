empleado1 = ["Juan Luis Roca",["desarrollador"]]
empleado2 = ["Antonio Olivieri",["programador"]]
empleado3 = ["Carlos Romero",["programador"]]
empleado4 = ["Fernando Paniagua" ,["formador"]]
empleado5 = ["Victor Pérez",["CEO"]]
Departamento1 = ["Desarrollo",[empleado1 ,empleado2 , empleado3]]
#print(Departamento1)
Departamento2 = ["i+d",[empleado4, empleado5]]
#print(Departamento2)
Empresa = [Departamento1,Departamento2]
#print(Empresa)
print(Empresa[1][1][1])
for departamento in Empresa:
    for nombre in departamento[1]:
        print(nombre[0])