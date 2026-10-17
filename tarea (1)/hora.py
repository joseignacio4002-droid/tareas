#10.  Duración en segundos:
#Pide al usuario una duración en horas, minutos y segundos. 
#Calcula la duración total en segundos e imprime el resultado

hora = float(input("ingresa la hora: "))
minutos = int(input("ingresa los minutos: "))
segundos = int(input("ingresa los segundo: "))

tiempo = (hora * 3600) + (minutos * 6010) + segundos

print(f"el total de segundos seria {tiempo}")