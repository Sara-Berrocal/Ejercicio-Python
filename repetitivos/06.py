import os 
os.system("cls")

n = int(input("Ingrese un numero: "))
x = int(input("Ingrese la cantidad inicial de x: "))
y = int(input("Ingrese la cantidad final de y: "))

for i in range(x, y + 1):
    print(f"{n} x {i} = {n * i} ")