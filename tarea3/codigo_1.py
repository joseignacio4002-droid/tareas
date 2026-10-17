from datetime import datetime
import pandas as pd


def cargar_escenas():
  return pd.read_excel("escenas_isla.xlsx")


def obtener_escena(df, id_actual):
  resultado = df[df["id_escena"] == id_actual]
  if not resultado.empty:
    return resultado.iloc[0]
  return None


def guardar_estado(escena_final, inventario, fila_final):
  estado = {
      "escena_final": escena_final,
      "inventario": ", ".join(inventario) if inventario else "sin objetos",
      "tipo_final": (
          fila_final["tipo_final"]
          if "tipo_final" in fila_final and pd.notna(fila_final["tipo_final"])
          else "desconocido"
      ),
      "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
  }
  pd.DataFrame([estado]).to_excel("estado_partida.xlsx", index=False)


def main():
  df_escenas = cargar_escenas()
  escena_actual = "inicio"
  inventario = []
  juego_activo = True

  while juego_activo:
    fila = obtener_escena(df_escenas, escena_actual)

    if fila is None:
      print("Error: No se encontró la escena actual en el mapa.")
      break

    print(f"\n{fila['descripcion']}")

    if pd.notna(fila["otorga_objeto"]) and fila["otorga_objeto"] != "":
      objeto = str(fila["otorga_objeto"]).strip()
      if objeto not in inventario:
        inventario.append(objeto)
        print(f"¡Has conseguido un nuevo objeto: {objeto}!")

    es_final_val = fila["es_final"]
    if isinstance(es_final_val, str):
      es_final = es_final_val.strip().upper() in ["TRUE", "SI", "1", "YES"]
    else:
      es_final = bool(es_final_val)

    if es_final:
      if pd.notna(fila["mensaje_final"]) and fila["mensaje_final"] != "":
        print(f"\n{fila['mensaje_final']}")
      print("\n--- FIN DEL JUEGO ---")
      guardar_estado(escena_actual, inventario, fila)
      juego_activo = False
    else:
      opciones_disponibles = {}

      op_a_texto = (
          str(fila["opcion_a"])
          if pd.notna(fila["opcion_a"]) and fila["opcion_a"] != ""
          else ""
      )
      op_b_texto = (
          str(fila["opcion_b"])
          if pd.notna(fila["opcion_b"]) and fila["opcion_b"] != ""
          else ""
      )

      req_a = (
          str(fila["requiere_objeto"])
          if "requiere_objeto" in fila
          and pd.notna(fila["requiere_objeto"])
          and fila["requiere_objeto"] != ""
          else ""
      )

      if op_a_texto:
        if req_a and req_a not in inventario:
          print(f"[Bloqueado] Opción A requiere: {req_a}")
        else:
          print(f"A) {op_a_texto}")
          opciones_disponibles["A"] = fila["destino_a"]

      if op_b_texto:
        print(f"B) {op_b_texto}")
        opciones_disponibles["B"] = fila["destino_b"]

      if not opciones_disponibles:
        print("No hay opciones disponibles. Fin de la aventura.")
        guardar_estado(escena_actual, inventario, fila)
        break

      eleccion = input("\nElige una opción: ").strip().upper()

      if eleccion in opciones_disponibles:
        escena_actual = str(opciones_disponibles[eleccion])
      else:
        print("Opción inválida o bloqueada. Inténtalo de nuevo.")


if __name__ == "__main__":
  main()