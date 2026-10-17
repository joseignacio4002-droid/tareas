# metro.py

METRO_CARACAS = {
    "Linea 1": {
        "Propatria": {"siguientes": ["Perez Bonalde"], "tiempo": 2},
        "Perez Bonalde": {"siguientes": ["Propatria", "Plaza Sucre"], "tiempo": 2},
        "Plaza Sucre": {"siguientes": ["Perez Bonalde", "Gato Negro"], "tiempo": 2},
        "Gato Negro": {"siguientes": ["Plaza Sucre", "Agua Salud"], "tiempo": 2},
        "Agua Salud": {"siguientes": ["Gato Negro", "Caño Amarillo"], "tiempo": 2},
        "Caño Amarillo": {"siguientes": ["Agua Salud", "Capitolio"], "tiempo": 2},
        "Capitolio": {"siguientes": ["Caño Amarillo", "La Hoyada"], "tiempo": 2},
        "La Hoyada": {"siguientes": ["Capitolio", "Parque Carabobo"], "tiempo": 2},
        "Parque Carabobo": {"siguientes": ["La Hoyada", "Bellas Artes"], "tiempo": 2},
        "Bellas Artes": {"siguientes": ["Parque Carabobo", "Colegio de Ingenieros"], "tiempo": 2},
        "Colegio de Ingenieros": {"siguientes": ["Bellas Artes", "Plaza Venezuela"], "tiempo": 2},
        "Plaza Venezuela": {"siguientes": ["Colegio de Ingenieros", "Sabana Grande", "Zona Rental", "Sabatino"], "tiempo": 2}, # Conecta con Línea 2/3 (Zona Rental)
        "Sabana Grande": {"siguientes": ["Plaza Venezuela", "Chacaito"], "tiempo": 2},
        "Chacaito": {"siguientes": ["Sabana Grande", "Chacao"], "tiempo": 2},
        "Chacao": {"siguientes": ["Chacaito", "Altamira"], "tiempo": 2},
        "Altamira": {"siguientes": ["Chacao", "Miranda"], "tiempo": 2},
        "Miranda": {"siguientes": ["Altamira", "Los Dos Caminos"], "tiempo": 2},
        "Los Dos Caminos": {"siguientes": ["Miranda", "Los Cortijos"], "tiempo": 2},
        "Los Cortijos": {"siguientes": ["Los Dos Caminos", "La California"], "tiempo": 2},
        "La California": {"siguientes": ["Los Cortijos", "Palo Verde"], "tiempo": 2},
        "Palo Verde": {"siguientes": ["La California"], "tiempo": 2}
    },
    "Linea 2": {
        "El Silencio": {"siguientes": ["Capuchinos"], "tiempo": 2},
        "Capuchinos": {"siguientes": ["El Silencio", "Maternidad", "Artigas"], "tiempo": 2}, # Conecta con Línea 4
        "Maternidad": {"siguientes": ["Capuchinos", "Artigas"], "tiempo": 2},
        "Artigas": {"siguientes": ["Maternidad", "La Paz"], "tiempo": 2},
        "La Paz": {"siguientes": ["Artigas", "La Yaguara"], "tiempo": 3},
        "La Yaguara": {"siguientes": ["La Paz", "Carapita"], "tiempo": 2},
        "Carapita": {"siguientes": ["La Yaguara", "Antímano"], "tiempo": 2},
        "Antímano": {"siguientes": ["Carapita", "Muelle"], "tiempo": 2},
        "Muelle": {"siguientes": ["Antímano", "Ruiz Pineda"], "tiempo": 2},
        "Ruiz Pineda": {"siguientes": ["Muelle", "Las Adjuntas"], "tiempo": 3},
        "Las Adjuntas": {"siguientes": ["Ruiz Pineda"], "tiempo": 0},
        # Ramal Zoológico
        "Zootecnia / Zoológico": {"siguientes": ["Caricuao"], "tiempo": 3}, # Simplificado como Zoológico
        "Caricuao": {"siguientes": ["Zootecnia / Zoológico", "Zoologico"], "tiempo": 3}
    },
    "Linea 3": {
        "Plaza Venezuela": {"siguientes": ["Tres Inciensos / C. Universitaria"], "tiempo": 2}, # Conexión virtual/real con L1
        "Ciudad Universitaria": {"siguientes": ["Plaza Venezuela", "Los Símbolos"], "tiempo": 2},
        "Los Símbolos": {"siguientes": ["Ciudad Universitaria", "La Bandera"], "tiempo": 2},
        "La Bandera": {"siguientes": ["Los Símbolos", "El Valle"], "tiempo": 2},
        "El Valle": {"siguientes": ["La Bandera", "Coche"], "tiempo": 3},
        "Coche": {"siguientes": ["El Valle", "La Rinconada"], "tiempo": 3},
        "La Rinconada": {"siguientes": ["Coche"], "tiempo": 0}
    },
    "Linea 4": {
        "Zona Rental": {"siguientes": ["Parque Central"], "tiempo": 2}, # Conexión con Línea 1 y 2
        "Parque Central": {"siguientes": ["Zona Rental", "Nuevo Circo"], "tiempo": 2},
        "Nuevo Circo": {"siguientes": ["Parque Central", "Teatros"], "tiempo": 2},
        "Teatros": {"siguientes": ["Nuevo Circo", "Capuchinos"], "tiempo": 2},
        "Capuchinos": {"siguientes": ["Teatros", "El Silencio"], "tiempo": 2} # Conexión con Línea 2
    }
}

def obtener_linea_de_estacion(nombre_estacion):
    """Devuelve una lista con las líneas a las que pertenece una estación."""
    lineas = []
    for linea, estaciones in METRO_CARACAS.items():
        if nombre_estacion in estaciones:
            lineas.append(linea)
    return lineas

def obtener_todas_las_estaciones():
    """Devuelve un conjunto con los nombres de todas las estaciones únicas."""
    estaciones = set()
    for linea in METRO_CARACAS.values():
        estaciones.update(linea.keys())
    return sorted(list(estaciones))