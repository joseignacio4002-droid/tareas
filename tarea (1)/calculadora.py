#1. Calculadora simple:
#Crea un programa que pida al usuario dos números y un operador (+, -, *, /).  
#Realiza la operación correspondiente e imprime el resultado.

print("bienvenido usuario")
numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese su segundo numero:"))
operacion = str(input("que operacion desea realizar: "))
if operacion == "suma":
    resultado = numero1 + numero2
    print(f"el resultado de su oprecion es {resultado}")

elif operacion == "resta":
    resultado = numero1 - numero2
    print(f"el resultado de su oprecion es {resultado}")

elif operacion == "division":
    resultado = numero1 / numero2
    print(f"el resultado de su oprecion es {resultado}")

elif operacion == "multiplicacion":
    resultado = numero1 * numero2 
    print(f"el resultado de su oprecion es {resultado}")

else:
    print("la opcion no es valida")
