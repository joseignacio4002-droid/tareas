#Pide al usuario un año. 
#Determina si el año es bisiesto. 
#Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


print("bienvenido al programa")
año = int(input("ingresa el año: "))

if (año % 4 == 0) and (año % 100 == 0) and (año % 400 == 0):
    print(f"el {año} es bisiesto")
else:
    print(f"el {año} no es bisiesto")