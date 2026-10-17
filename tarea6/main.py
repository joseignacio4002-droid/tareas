# main.py
from metro import obtener_todas_las_estaciones, obtener_linea_de_estacion, METRO_CARACAS
from planificador import calcular_ruta_optima

def mostrar_menu():
    print("\n========================================")
    print("      🚇 SIMULADOR METRO DE CARACAS     ")
    print("========================================")
    print("1. Planificar viaje (Calcular Ruta)")
    print("2. Consultar líneas de una estación")
    print("3. Listar todas las estaciones")
    print("4. Salir")
    print("=========================================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            print("\n--- Planificador de Rutas ---")
            origen = input("Ingrese la estación de origen: ").strip().title()
            destino = input("Ingrese la estación de destino: ").strip().title()

            ruta, tiempo, transbordos = calcular_ruta_optima(origen, destino)

            if not ruta:
                print("\n❌ Error: Alguna de las estaciones ingresadas no es válida o no existe conexión.")
                continue

            print(f"\n✅ ¡Ruta calculada con éxito!")
            print(f"📍 **Origen:** {origen}")
            print(f"🏁 **Destino:** {destino}")
            print(f"⏱️ **Tiempo estimado total:** {tiempo} minutos")
            print(f"🚉 **Estaciones recorridas:** {len(ruta)}")
            
            print("\n--- Itinerario del Viaje ---")
            for i, est in enumerate(ruta):
                lineas = ", ".join(obtener_linea_de_estacion(est))
                print(f"  {i+1}. {est} (Líneas: {lineas})")

            if transbordos:
                print("\n🔄 **Avisos de Cambio de Línea:**")
                for est_transbordo, nueva_lin in transbordos:
                    print(f"   ⚠️ En la estación **{est_transbordo}**, realiza transferencia hacia la **{nueva_lin}**.")
            else:
                print("\n✨ Viaje directo: No necesitas realizar cambios de línea.")

        elif opcion == "2":
            estacion = input("\nIngrese el nombre de la estación a consultar: ").strip().title()
            lineas = obtener_linea_de_estacion(estacion)
            if lineas:
                print(f"📌 La estación **{estacion}** pertenece a: {', '.join(lineas)}")
            else:
                print("❌ Estación no encontrada.")

        elif opcion == "3":
            print("\n--- Estaciones del Sistema ---")
            estaciones = obtener_todas_las_estaciones()
            for est in estaciones:
                lineas = ", ".join(obtener_linea_de_estacion(est))
                print(f"• {est} [{lineas}]")

        elif opcion == "4":
            print("\n¡Gracias por usar el simulador del Metro de Caracas! ¡Buen viaje! 🚆")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()