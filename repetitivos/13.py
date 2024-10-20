import os
os.system("cls")

n = int(input("Ingrese el valor de n: "))

suma = 0

for i in range(1, n+1):
    if i % 3 == 0:
        if i % 5 != 0:
            suma += i

print("La suma de los multtiplos de 3 pero no de 5 es:", suma)
