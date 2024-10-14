import os 
os.system("cls")

ausencia = float(input("Ingrese horas de ausencia al trabajo: "))
defectuoso = int(input("Ingrese la cantidad de tornillos defectuosos: "))
nodefectuoso = int(input("Ingrese la cantidad de tornillo no defectuoso: "))

condicion1 = ausencia <= 1.5
condicion2 = defectuoso < 300
condicion3 = nodefectuoso > 10000

if condicion1 and condicion2 and condicion3:
        grado = 20
elif condicion1 and condicion2:
    grado = 12
elif condicion1 and condicion3: 
    grado = 13
elif condicion2 and condicion3:
    grado = 15
elif condicion1:
    grado = 7 
elif condicion2:
    grado = 8
elif condicion3:
    grado = 9
else: 
    grado = 5
    
print("El grado de eficiencia del operario es:", grado)

# import os
# os.system("cls")

# hAusencia = float(input("Hora Ausencia: ")) < 1.5
# tmalos = int(input("Tornillos malos: ")) < 300
# tbuenos = int(input("Tornillos buenos: ")) > 10000

# if not hAusencia and not tmalos and not tbuenos: print("Grado 5")
# if  hAusencia and not tmalos and not tbuenos: print("Grado 7")
# if not hAusencia and tmalos and not tbuenos: print("Grado 8")
# if not hAusencia and not tmalos and  tbuenos: print("Grado 9")