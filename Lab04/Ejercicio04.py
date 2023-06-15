import math

# Función para resolver la tercera ley de Kepler
def resolver_tercera_ley_kepler(periodo, semieje, M):
    # Calcular la masa del cuerpo central
    masa_central = 4 * math.pi**2 * semieje**3 / periodo**2
    # Calcular la masa del objeto en movimiento
    masa_objeto = masa_central - M
    return masa_central, masa_objeto

# Diccionario de tuplas con los períodos y semiejes mayores de los planetas
datos_planetas = {
    "Mercurio": (0.2408467, 0.387),
    "Venus": (0.61519726, 0.723),
    "Tierra": (1.0, 1.0),
    "Marte": (1.8808476, 1.523),
    "Júpiter": (11.862, 5.203),
    "Saturno": (29.457, 9.537),
    "Urano": (84.017, 19.191),
    "Neptuno": (164.79132, 30.069),
    "Plutón": (248.0, 39.482)
}

# Solicitar al usuario el planeta deseado
planeta = input("Ingresa el nombre de un planeta del sistema solar: ")

# Verificar si el planeta está en el diccionario de datos
if planeta in datos_planetas:
    periodo, semieje = datos_planetas[planeta]
    # Masa total del sistema
    M = 1.989 * 10**30 # Masa del Sol en kg
    # Resolver la tercera ley de Kepler
    masa_central, masa_objeto = resolver_tercera_ley_kepler(periodo, semieje, M)
    print("Resultados para el planeta", planeta)
    print("Masa del cuerpo central (masa del Sol):", masa_central)
    print("Masa del objeto en movimiento (masa del planeta):", masa_objeto)
else:
    print("El planeta", planeta, "no se encuentra en el diccionario de datos.")
