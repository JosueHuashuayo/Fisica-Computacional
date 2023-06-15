import math
import numpy as np

# Función para calcular el área barrida en un intervalo de tiempo
def calcular_area(t, r):
    area = 0.0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        area += 0.5 * (r[i] + r[i-1]) * dt
    return area

# Función para resolver la segunda ley de Kepler
def resolver_segunda_ley_kepler(t, r, M):
    # Calcular el área total barrida
    area_total = calcular_area(t, r)
    # Calcular el tiempo promedio
    t_promedio = np.mean(t)
    # Calcular la constante angular (constante de proporcionalidad)
    k = area_total / (t_promedio**2)
    # Calcular la masa del cuerpo central
    masa_central = k / (4 * math.pi**2)
    # Calcular la masa del objeto en movimiento
    masa_objeto = M - masa_central
    return masa_central, masa_objeto

# Datos de masa y radio de los planetas en kg y metros
masas_planetas = {
    "Mercurio": 3.3011e23,
    "Venus": 4.8675e24,
    "Tierra": 5.97237e24,
    "Marte": 6.4171e23,
    "Júpiter": 1.8982e27,
    "Saturno": 5.6834e26,
    "Urano": 8.6810e25,
    "Neptuno": 1.02413e26,
    "Plutón": 1.303e22
}

# Solicitar al usuario el planeta deseado
planeta = input("Ingresa el nombre de un planeta del sistema solar: ")

# Verificar si el planeta está en la lista de planetas conocidos
if planeta in masas_planetas:
    masa_planeta = masas_planetas[planeta]
    # Datos de tiempo y radio en unidades arbitrarias
    t = np.array([0, 1, 2, 3, 4, 5]) # Tiempo
    r = np.array([1, 2, 3, 4, 5, 6]) # Radio
    # Masa total del sistema
    M = masa_planeta
    # Resolver la segunda ley de Kepler
    masa_central, masa_objeto = resolver_segunda_ley_kepler(t, r, M)
