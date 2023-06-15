import math

# Función para calcular la densidad en un planeta específico
def calcular_densidad(planeta):
    # Diccionario con las masas y radios de los planetas en kg y m respectivamente
    planetas = {
        "Mercurio": (3.3011e23, 2.4397e6),
        "Venus": (4.8675e24, 6.0518e6),
        "Tierra": (5.97237e24, 6.371e6),
        "Marte": (6.4171e23, 3.3895e6),
        "Júpiter": (1.8982e27, 6.9911e7),
        "Saturno": (5.6834e26, 5.8232e7),
        "Urano": (8.6810e25, 2.5362e7),
        "Neptuno": (1.02413e26, 2.4622e7),
        "Plutón": (1.303e22, 1.1883e6)
    }
    
    # Verificar si el planeta está en el diccionario de planetas conocidos
    if planeta in planetas:
        masa_planeta, radio_planeta = planetas[planeta]
        volumen_planeta = (4/3) * math.pi * (radio_planeta**3)
        #Calcular la densidad utilizando la fórmula Densidad = Masa / Volumen
        densidad = masa_planeta / volumen_planeta
        return densidad
    else:
        return None

planeta = input("Ingresa el nombre de un planeta del sistema solar: ")
densidad_planeta = calcular_densidad(planeta)

if densidad_planeta:
    print(f"La densidad en {planeta} es de {densidad_planeta:.2f} kg/m^3.")
else:
    print("El planeta ingresado no está en la lista de planetas conocidos.")
