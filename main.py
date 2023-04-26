import gpsd
import random

def buscar_frecuencia_vacia():
    # Conectar al demonio de GPSD
    gpsd.connect()

    # Obtener la ubicación del dispositivo
    packet = gpsd.get_current()
    latitud = packet.lat
    longitud = packet.lon

    # Calcular una frecuencia de radio vacía basada en la ubicación
    frecuencia_min = 88.1 # Frecuencia mínima disponible
    frecuencia_max = 107.9 # Frecuencia máxima disponible
    frecuencia = None

    # Generar una lista de frecuencias disponibles en el rango dado
    frecuencias_disponibles = [f for f in range(int(frecuencia_min * 10), int(frecuencia_max * 10) + 1)]

    # Bucle para buscar una frecuencia vacía
    while not frecuencia:
        # Obtener una frecuencia al azar de la lista de frecuencias disponibles
        frecuencia_random = random.choice(frecuencias_disponibles)

        # Comprobar si la frecuencia está ocupada (por ejemplo, mediante un escaneo de radio)
        if not frecuencia_ocupada(frecuencia_random):
            frecuencia = frecuencia_random / 10.0 # Convertir la frecuencia de entero a float

    return frecuencia

def frecuencia_ocupada(frecuencia):
    # Función ficticia para verificar si una frecuencia de radio está ocupada
    # Aquí podrías implementar la lógica real para escanear las frecuencias y verificar si están ocupadas
    # Por ejemplo, puedes utilizar una librería de escaneo de radio o realizar una consulta a una base de datos de frecuencias ocupadas en tu área
    # Retorna True si la frecuencia está ocupada, False si está disponible
    # Este es solo un ejemplo básico y no representa una implementación real

    # En este ejemplo, asumimos que una frecuencia está ocupada si el último dígito es 5 (por ejemplo, 88.5, 89.5, etc.)
    if frecuencia % 10 == 5:
        return True
    else:
        return False

buscar_frecuencia_vacia()