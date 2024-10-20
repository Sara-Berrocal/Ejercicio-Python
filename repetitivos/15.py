import os 
os.system("cls")

texto1 = input("Ingrese una cadena de texto: ")
opcion= input("Escribe 'M' para convertirlo en mayusculas o 'm' para convertirlo en minusculas: ")

if opcion == 'M':
    textconvertido = texto1.upper()

elif opcion == 'm':
    textconvertido = texto1.lower()
    
else:
    textconvertido = "Opcion no valida"

print("El texto convertido es:", textconvertido)
