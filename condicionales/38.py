def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
def diasmes(mes, año):
    nom = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias = [31, 29 if bisiesto(año) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (nom[mes-1], dias[mes-1]) if 1 <= mes <= 12 else ("Mes invalido", 0)

mes = int(input("Mes (1-12): "))
año = int(input("Año: "))
nom, dias = diasmes(mes, año)
print(f"{nom} tiene {dias} dias:" if dias > 0 else "Mes invalido.")
