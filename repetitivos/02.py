import os 
os.system("cls")

def multiplicar (n1, n2):
  
    producto = 0
    while n2 > 0:
      n2 -= 1
      producto += n1
    return producto

multiplicando = int(input("Ingrese el multiplicando: "))
multiplicador = int(input("Ingrese el multiplicador: "))

print(f"Producto = {multiplicar(multiplicando, multiplicador)}")



# multiplicando = int(input("Ingrese el multiplicando: "))
# multiplicador = int(input("Ingrese el multiplicador: "))

# producto = 0

# while multiplicador > 0:
#     multiplicador -= 1
#     producto      += multiplicando

# print(f"Producto = {producto}")

