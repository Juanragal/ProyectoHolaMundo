importe1 = float(input("Introduce el valor del importe 1:"))
importe2 = float(input("Introduce el valor del importe 2:"))
impuesto = float(input ("Introduce el valor del impuesto del Valor Añadido a aplicar:(%)"))
impuesto = 1+impuesto/100
valor = impuesto*(importe1+importe2)
print("importe de la factura" , valor)