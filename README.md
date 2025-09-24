# Simulación (SCD1022)

Este repositorio aloja el proyecto final de la experiencia educativa
**Simulación**, donde se modelan sistemas mediante métodos numéricos y
estocásticos.  Se incluyen tres experimentos de simulación escritos en
Python para ilustrar distintos conceptos del curso.

## Contenido

* `estimar_pi` – Emplea el método Monte Carlo para aproximar el valor de π.
  Genera puntos aleatorios en un cuadrado y calcula la proporción que cae
  dentro de un círculo inscrito.
* `caminata_aleatoria` – Implementa una caminata aleatoria en una dimensión
  para analizar el comportamiento de procesos al azar.
* `simular_mm1` – Simula un sistema de colas M/M/1 con llegadas y servicios
  exponenciales.  Devuelve el tiempo promedio en el sistema y el número
  máximo de clientes en cola.

El código se encuentra en el módulo [`simulation.py`](simulation.py) y
incluye un bloque `__main__` con ejemplos de ejecución.

## Temario de la experiencia educativa

Entre los temas tratados en la asignatura se encuentran:

1. Generación de variables aleatorias y métodos Monte Carlo.
2. Simulación de sistemas de colas y cadenas de Markov.
3. Modelado de procesos estocásticos (caminatas aleatorias, procesos de Poisson).
4. Diseño de experimentos y análisis estadístico de resultados.

Las simulaciones aquí implementadas constituyen una introducción a estos
temas y sirven como base para estudios más avanzados de simulación.
