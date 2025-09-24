"""
Simulaciones para la materia de Simulación (SCD1022).

La simulación permite analizar sistemas complejos mediante modelos
probabilísticos y estocásticos.  Este módulo implementa tres simulaciones
clásicas:

1. **Estimación de π** utilizando el método Monte Carlo.
2. **Caminata aleatoria** en una dimensión para estudiar procesos de azar.
3. **Sistema M/M/1** (cola de Poisson) para modelar tiempos de llegada y servicio.

Cada función devuelve métricas relevantes del experimento.  Se pueden
ajustar los parámetros para experimentar con diferentes configuraciones.
"""

import random
import math
from typing import List, Tuple


def estimar_pi(iteraciones: int = 100000) -> float:
    """Estima el valor de π usando el método Monte Carlo.

    Se generan puntos uniformemente distribuidos en el cuadrado [0,1] x [0,1]
    y se calcula la proporción que cae dentro del círculo de radio 1.

    :param iteraciones: Número de puntos aleatorios a generar.
    :returns: Aproximación de π.
    """
    dentro = 0
    for _ in range(iteraciones):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            dentro += 1
    return 4.0 * dentro / iteraciones


def caminata_aleatoria(pasos: int = 1000) -> int:
    """Realiza una caminata aleatoria en una dimensión.

    En cada paso, la posición se incrementa o decrementa en 1 con igual
    probabilidad.  Se devuelve la posición final después de `pasos` pasos.

    :param pasos: Número de pasos en la caminata.
    :returns: Posición final del caminante.
    """
    posicion = 0
    for _ in range(pasos):
        posicion += 1 if random.random() < 0.5 else -1
    return posicion


def simular_mm1(lambda_arr: float, mu: float, tiempo_max: float = 1000.0) -> Tuple[float, int]:
    """Simula un sistema de colas M/M/1.

    Genera llegadas según un proceso de Poisson con tasa `lambda_arr` y
    tiempos de servicio exponenciales con tasa `mu`.  Utiliza el método de
    eventos discretos para procesar llegadas y salidas.  Calcula el tiempo
    promedio en el sistema y el número máximo de clientes en cola.

    :param lambda_arr: Tasa de llegadas (clientes/tiempo).
    :param mu: Tasa de servicio.
    :param tiempo_max: Tiempo total de simulación.
    :returns: Tupla `(tiempo_promedio, max_en_cola)`.
    """
    import heapq
    reloj = 0.0
    cola: List[float] = []
    eventos: List[Tuple[float, str]] = []  # (tiempo, tipo)
    num_en_sistema = 0
    tiempos_en_sistema: List[float] = []
    max_en_cola = 0

    # Programar primera llegada
    heapq.heappush(eventos, (reloj + random.expovariate(lambda_arr), 'llegada'))

    while eventos:
        tiempo_evento, tipo = heapq.heappop(eventos)
        if tiempo_evento > tiempo_max:
            break
        reloj = tiempo_evento
        if tipo == 'llegada':
            num_en_sistema += 1
            cola.append(reloj)
            max_en_cola = max(max_en_cola, num_en_sistema - 1)
            # Programar siguiente llegada
            heapq.heappush(eventos, (reloj + random.expovariate(lambda_arr), 'llegada'))
            # Si el servidor está libre (solo este cliente en el sistema), programar su salida
            if num_en_sistema == 1:
                servicio = random.expovariate(mu)
                heapq.heappush(eventos, (reloj + servicio, 'salida'))
        else:  # salida
            llegada_cliente = cola.pop(0)
            tiempos_en_sistema.append(reloj - llegada_cliente)
            num_en_sistema -= 1
            # Si hay clientes esperando, programar salida del siguiente
            if num_en_sistema > 0:
                servicio = random.expovariate(mu)
                heapq.heappush(eventos, (reloj + servicio, 'salida'))

    tiempo_promedio = (sum(tiempos_en_sistema) / len(tiempos_en_sistema)) if tiempos_en_sistema else 0.0
    return tiempo_promedio, max_en_cola


if __name__ == "__main__":
    # Ejemplo de estimación de pi
    print("Estimación de π:", estimar_pi(50000))
    # Ejemplo de caminata aleatoria
    print("Posición final de una caminata aleatoria de 100 pasos:", caminata_aleatoria(100))
    # Ejemplo de simulación M/M/1
    promedio, max_cola = simular_mm1(lambda_arr=2.0, mu=3.0, tiempo_max=100.0)
    print(f"Tiempo promedio en el sistema: {promedio:.2f}, Máx. en cola: {max_cola}")