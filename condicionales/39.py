def calcugrado(ausencia, defectuoso, nodefectuoso):
    if ausencia <= 1.5 and defectuoso < 300 and nodefectuoso > 10000:
        return 20
    elif ausencia <= 1.5 and defectuoso < 300:
        return 12
    elif ausencia <= 1.5 and nodefectuoso > 10000:
        return 13
    elif defectuoso < 300 and nodefectuoso > 10000:
        return 15
    elif ausencia <= 1.5:
        return 7 
    elif defectuoso < 300:
        return 8
    elif nodefectuoso > 10000:
        return 9
    else: 
        return 5
    
try:    
    ausencia = float(input("Ingrese horas de ausencia al trabajo: "))
    defectuoso = int(input("Ingrese la cantidad de tornillos defectuosos: "))
    nodefectuoso = int(input("Ingrese la cantidad de tornillo no defectuoso: "))

    grado = calcugrado(ausencia, defectuoso, nodefectuoso)
    print(f"El grado de eficiencia del operario es: {grado}")
except ValueError:
    print("Ingrese un valor numerico valido.")