from functools import wraps

def agente_d(func):
    """Decorador de infiltración 'Agente D' para espionaje de funciones."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[INFORME]: ¡Agente D infiltrando al objetivo '{func.__name__}'!")
        print(f"[INTELIGENCIA]: Equipamiento táctico (args) detectado: {args}")
        print(f"[INTELIGENCIA]: Documentos secretos (kwargs) recuperados: {kwargs}")
        
        
        resultado = func(*args, **kwargs)
        
        print(f"[EXTRACCIÓN]: ¡Misión cumplida! El objetivo ha revelado el secreto: {resultado!r}")
        return resultado
        
    return wrapper

@agente_d
def revisar_caja_roja(codigo_acceso):
    if codigo_acceso == "alfa-77":
        return "¡Bomba encontrada y desactivada en caja roja!"
    return "Caja vacía... falso positivo."

@agente_d
def revisar_caja_azul(codigo_acceso, nivel_alerta=1):
    if codigo_acceso == "omega-99" and nivel_alerta > 2:
        return "¡Bomba encontrada y desactivada en caja azul!"
    return "Zona despejada. No hay amenaza."

@agente_d
def revisar_caja_verde(codigo_acceso, autorizacion=False):
    if autorizacion and codigo_acceso == "delta-01":
        return "¡Bomba encontrada y desactivada en caja verde!"
    return "Sin rastros de explosivos."

if __name__ == "__main__":
    print("--- INICIANDO BARRIDO DE INTELIGENCIA EN TODAS LAS BASES ---")
    
    
    objetivos = [
        lambda: revisar_caja_roja("beta-12"),
        lambda: revisar_caja_azul("omega-99", nivel_alerta=1),
        lambda: revisar_caja_verde("delta-01", autorizacion=True)
    ]
    
    
    for i, mision in enumerate(objetivos, 1):
        print(f"\n> Analizando sector {i}")
        resultado_mision = mision()
        
        
        if "¡Bomba encontrada" in resultado_mision:
            print(f" [ALERTA MÁXIMA]: ¡El objetivo correcto ha sido localizado en el sector {i}!")
            break