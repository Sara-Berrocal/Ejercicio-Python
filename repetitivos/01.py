import os 
os.system("cls")

dividendo = 18
divisor   = 5

cociente = 0
resto    = dividendo

while resto >= divisor:
    resto -= divisor
    cociente += 1

print(f"El cociente de la division de {dividendo} entre {divisor} es {cociente} y el resto es {resto}")