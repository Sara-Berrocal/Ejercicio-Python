import os 
os.system("cls")

resultado = 0

multiplicar = (a, b)
if a < 0:
    a = -a
if b < 0:
    b = -b

for _ in range(b):
    resultado += a

nume1 = int(input("Ingresa el primer numero: "))
nume2 = int(input("Ingresa el segundo numero: "))

print(f"El resultado de multiplicar {nume1} y {nume2} es: ")