import os 
os.system("cls")
edad1 = int(input("Ingrese la primera edad: "))
edad2 = int(input("Ingrese la segunda edad: "))
edad3 = int(input("Ingrese la tercera edad: "))

edadmay = max(edad1, edad2, edad3)
edadmmen = min (edad1, edad2, edad3)

print(f"La edad mayor es: {edadmay}")
print(f"La edad menor es: {edadmmen}")

