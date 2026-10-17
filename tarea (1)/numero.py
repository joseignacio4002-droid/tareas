#4.  Número par o impar:
#Pide al usuario un número. 
#Determina si el número es par o impar usando el operador módulo (%) e imprime el resultado.

print("bienvenido usuario")
numero = float(input("ingrese un numero: "))
if numero % 2 == 0:
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar") 