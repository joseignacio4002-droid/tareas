# planificador.py
from collections import deque
from metro import METRO_CARACAS, obtener_linea_de_estacion

def construir_grafo_general():
    """Construye un grafo unificado de adyacencias considerando todas las líneas."""
    grafo = {}
    for linea, estaciones in METRO_CARACAS.items():
        for est, datos in estaciones.items():
            if est not in grafo:
                grafo[est] = []
            for vec in datos["siguientes"]:
                # Guardamos el vecino y la línea actual
                grafo[est].append((vec, linea, datos["tiempo"]))
    return grafo

def calcular_ruta_optima(origen, destino):
    """
    Calcula la ruta óptima entre origen y destino usando BFS.
    Retorna: (secuencia_estaciones, tiempo_total, transbordos)
    """
    if origen not in [e for l in METRO_CARACAS.values() for e in l] or \
       destino not in [e for l in METRO_CARACAS.values() for e in l]:
        return None, 0, []

    if origen == destino:
        return [origen], 0, []

    grafo = construir_grafo_general()
    
    # Cola para BFS: almacena (estacion_actual, ruta_hasta_aqui, tiempo_acumulado, linea_actual)
    # Nota: Para simplificar el BFS puro de estaciones
    cola = deque([(origen, [origen], 0, None)])
    visitados = {origen}

    while cola:
        estacion_actual, ruta, tiempo_acumulado, linea_actual = cola.popleft()

        if estacion_actual == destino:
            # Procesar transbordos a partir de la ruta obtenida
            transbordos = detectar_transbordos(ruta)
            return ruta, tiempo_acumulado, transbordos

        for vecino, linea_vecino, peso in grafo.get(estacion_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, ruta + [vecino], tiempo_acumulado + peso, linea_vecino))

    return None, 0, []

def detectar_transbordos(ruta):
    """Analiza la ruta estación por estación para identificar en dónde se cambia de línea."""
    transbordos = []
    linea_actual = None
    
    for i in range(len(ruta) - 1):
        est_actual = ruta[i]
        est_siguiente = ruta[i+1]
        
        # Encontrar qué líneas comparten ambas estaciones o cuál línea conecta
        lineas_actuales = set(obtener_linea_de_estacion(est_actual))
        lineas_siguientes = set(obtener_linea_de_estacion(est_siguiente))
        
        comunes = lineas_actuales.intersection(lineas_siguientes)
        
        if linea_actual is None:
            # Tomar la primera línea disponible que conecte con la siguiente
            linea_actual = list(lineas_actuales.intersection(lineas_siguientes))[0] if comunes else list(lineas_actuales)[0]
        
        # Si la línea actual no está en las líneas de la siguiente estación, ocurrió un transbordo
        if not comunes or linea_actual not in comunes:
            # Buscar nueva línea
            nueva_linea = list(lineas_actuales.intersection(lineas_siguientes))
            if not nueva_linea:
                # Transbordo en estación común (ej. Plaza Venezuela / Zona Rental)
                for l in lineas_siguientes:
                    if l != linea_actual:
                        nueva_linea = [l]
                        break
            if nueva_linea:
                linea_actual = nueva_linea[0]
                transbordos.append((est_actual, linea_actual))
                
    return transbordos