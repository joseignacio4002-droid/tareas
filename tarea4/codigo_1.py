base_de_datos_dinosaurios = [
    ("Tyrannosaurus Rex", "Rex", "Carnívoro", "Cretácico"),
    ("Velociraptor", "Raptor", "Carnívoro", "Cretácico"),
    ("Triceratops", "Prorsus", "Herbívoro", "Cretácico"),
    ("Brachiosaurus", "Brachiosaurus", "Herbívoro", "Jurásico"),
    ("Stegosaurus", "Armatus", "Herbívoro", "Jurásico"),
    ("Spinosaurus", "Aegyptiacus", "Carnívoro", "Cretácico")
]

def informacion_dinosaurio(base_de_datos, nombre_dinosaurio):
    encontrado = False
    for dino in base_de_datos:
        
        if dino[0].lower() == nombre_dinosaurio.lower():
            print(f"Nombre: {dino[0]}, Especie: {dino[1]}, Dieta: {dino[2]}, Período: {dino[3]}")
            encontrado = True
            break
            
    if not encontrado:
        print("Dinosaurio no encontrado.")

def dinosaurios_por_dieta(base_de_datos, dieta):
    encontrados = False
    print(f"\n--- Dinosaurios con dieta: {dieta} ---")
    for dino in base_de_datos:
        if dino[2].lower() == dieta.lower():
            print(f"Nombre: {dino[0]}, Especie: {dino[1]}, Dieta: {dino[2]}, Período: {dino[3]}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron dinosaurios con esa dieta en el sistema.")


def dinosaurios_por_periodo(base_de_datos, periodo):
    encontrados = False
    print(f"\n--- Dinosaurios del período: {periodo} ---")
    for dino in base_de_datos:
        if dino[3].lower() == periodo.lower():
            print(f"Nombre: {dino[0]}, Especie: {dino[1]}, Dieta: {dino[2]}, Período: {dino[3]}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron dinosaurios en ese período en el sistema.")

def sistema_jurassic_park():
    while True:
        print("\n========================================")
        print("   SISTEMA DE CONTROL DE JURASSIC PARK  ")
        print("========================================")
        print("1. Buscar dinosaurio por nombre")
        print("2. Buscar dinosaurios por dieta")
        print("3. Buscar dinosaurios por período")
        print("4. Salir del sistema")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del dinosaurio: ")
            informacion_dinosaurio(base_de_datos_dinosaurios, nombre)
            
        elif opcion == "2":
            dieta = input("Ingrese el tipo de dieta (Carnívoro / Herbívoro / Omnívoro): ")
            dinosaurios_por_dieta(base_de_datos_dinosaurios, dieta)
            
        elif opcion == "3":
            periodo = input("Ingrese el período (Cretácico / Jurásico / Triásico): ")
            dinosaurios_por_periodo(base_de_datos_dinosaurios, periodo)
            
        elif opcion == "4":
            print("\nCerrando sesión de seguridad... ¡Cuidado con los velociraptors sueltos!")
            break
            
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número entre 1 y 4.")

sistema_jurassic_park()