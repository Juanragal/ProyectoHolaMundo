tupla = (("Enero",10000),("Febrero",3000),("Marzo",5000))
NOMBRE_FICHERO="Plantilla.html"
fichero=open(NOMBRE_FICHERO, "w") 
fichero.write("<!DOCTYPE html>\n")
fichero.write("<html lang=\"es\">\n")
fichero.write("<head>\n")
fichero.write("    <title>Tabla de ventas</title>\n")
fichero.write("<body>\n")
fichero.write("    <h1>Ventas anuales</h1>\n")
fichero.write("    <table>\n")
fichero.write("        <tr>\n")
fichero.write("            <td>Mes</td>\n")
fichero.write("            <td>Ventas</td>\n")
fichero.write("        </tr>\n")
for i in tupla:
    fichero.write("        <tr>\n")
    fichero.write("            <td>"+i[0]+"</td>\n")
    fichero.write("            <td>"+str(i[1])+"</td>\n")
    fichero.write("        </tr>\n")
fichero.write("    </table>\n")
fichero.write("</body>\n")
fichero.write("</html>\n")
fichero.close()