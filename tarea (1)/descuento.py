#7.  Calculadora de descuento:
#Pide al usuario el precio de un producto y el porcentaje de descuento. 
#Calcula el precio final después del descuento e imprime el resultado.
print("bienvenido al programa")
precio = int(input("ingresa el precio del producto: "))
descuento = int(input("ingresa el descuento: "))

descuento_total = (precio * 0.20)
precio -= descuento_total

print(f"el precio total es de {precio}")
print(f"el descuento total es de {descuento_total}")