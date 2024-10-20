import os 
os.system("cls")

numero = int(input("Ingrese un numero entero: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo.")