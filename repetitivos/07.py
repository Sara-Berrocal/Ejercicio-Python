import os 
os.system ("cls")

def factorial (n):
    rpta= 1
    while n > 1 :
        rpta *= n
        n -= 1
    return rpta

def factorial (n):
    return factorial

def factorial_r(n):
    if n == 1 : return 1
    return n * factorial_r (n-1)

numero = int(input("Numero : ")) 

print(f"Factorial = {factorial_r(numero) }")

 

# numero = int(input("Numero : ")) 
# factorial = 1
# while numero > 1:
#      factorial *= numero
#      numero -= 1

# print(f"Factorial = {factorial}")

