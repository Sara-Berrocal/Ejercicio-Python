import os 
os.system("cls")

n = int(input("Numero: "))
m = int(input("Cantidad de multiplos: "))
print([n * i for i in range(1, m+1)])