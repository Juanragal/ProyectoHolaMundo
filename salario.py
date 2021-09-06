from win10toast import ToastNotifier
salario = input("introduce tu salario anual:")
if salario.isdigit():
    salario = int(salario)
    pagas = int(input("En cuantas pagas lo quieres dividir (12 o 14)"))
    mensual = salario / pagas
    print("tu salario mensual es de",mensual, "por", pagas, "meses")
    toaster = ToastNotifier()
    toaster.show_toast("Juanra Project","Tu salario mensual es"+str(mensual))
elif salario[0]=="-":
    print("El salario no puede ser negativo....")
else:
    print("El salario bruto es erroneo")
