import math

def calcular_gravedad(planeta):
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
    masa_sol = 1.989e30
    radio_sol = 6.9634e8
    G = 6.67430e-11

    if planeta in planetas:
        masa_planeta, radio_planeta = planetas[planeta]
        gravedad = (G * masa_planeta) / (radio_planeta ** 2)
        gravedad_relativa = gravedad / ((G * masa_sol) / (radio_sol ** 2))
        return gravedad, gravedad_relativa
    else:
        return None, None

planeta = input("Ingresa el nombre de un planeta del sistema solar: ")
gravedad_planeta, gravedad_relativa_planeta = calcular_gravedad(planeta)

if gravedad_planeta and gravedad_relativa_planeta:
    print(f"La gravedad en {planeta} es de {gravedad_planeta:.2f} m/s^2.")
    print(f"La gravedad relativa en {planeta} respecto a la Tierra es de {gravedad_relativa_planeta:.2f}.")
else:
    print("El planeta ingresado no está en la lista de planetas conocidos.")
