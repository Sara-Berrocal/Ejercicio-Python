import os
os.system("cls")

nume = int(input("Ingrese un numero entero: "))
cantdivisores = sum(1 for i in range(1, nume + 1) if nume % i == 0)
print(f"La cantidad de divisores de {nume} es: {cantdivisores}")
