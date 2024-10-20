import os
os.system("cls")

contador = 0
for numero in range(100, 1000):

    centenas = numero // 100
    unidades = numero % 10

    if centenas == unidades:
        contador += 1

print("Cantidad de numeros capicuas de 3 cifras:", contador)

