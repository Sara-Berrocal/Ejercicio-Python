import os 
os.system("cls")

# dividendo = 18
# divisor   = 5

# cociente = 0
# resto    = dividendo

# while resto >= divisor:
#     resto -= divisor
#     cociente += 1

# print(f"El cociente de la division de {dividendo} entre {divisor} es {cociente} y el resto es {resto}")

dividendo = int(input("Dividendo: "))
divisor   = int(input("Divisor: "))

cociente = 0
while dividendo >= divisor:
    cociente += 1         #cociente = cociente + 1
    dividendo -= divisor  # dividendo = dividendo - divisor

print(f"Cociente = {cociente}")
print(f"Residuo = {dividendo}")