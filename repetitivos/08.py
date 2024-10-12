import os
os.system("cls")

n = int(input("Ingrese la base(n): "))
m = int(input("Ingrese el exponente(m): "))
potencia = 1

for i in range(m):
  potencia *= n

print(f"{n} elevado a la {m} es: {potencia} ")