import os 
os.system("cls")

numeros = []
suma = 0

for i in range(10):
    numero = float(input("Ingrese un numero: "))
    numeros.append(numero)
    suma += numero

menor = numeros[0]
mayor = numeros[0]

for num in numeros:
    if num < menor:
        menor = num
    if num > mayor:
        mayor = num

promedio = suma / 10 

print("El menor numero es:", menor)
print("El mayor numero es:", mayor)
print("El promedio es:", promedio)
