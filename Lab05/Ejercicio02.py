# Definición de la función para resolver la ecuación de Bernoulli
def ecuacion_bernoulli(p1, v1, h1, p2, v2, h2):
    if p1 is None:
        p1 = p2 + 0.5 * rho * v2**2 + rho * g * h2 - rho * g * h1
    elif p2 is None:
        p2 = p1 - 0.5 * rho * v1**2 - rho * g * h1 + rho * g * h2
    elif v1 is None:
        v1 = (2*(p1-p2) + rho*g*(h1-h2)) / rho
    elif v2 is None:
        v2 = (2*(p2-p1) + rho*g*(h2-h1)) / rho
    elif h1 is None:
        h1 = h2 + (p1 - p2 + 0.5 * rho * v2**2 - 0.5 * rho * v1**2) / (rho * g)
    elif h2 is None:
        h2 = h1 - (p1 - p2 + 0.5 * rho * v2**2 - 0.5 * rho * v1**2) / (rho * g)
    
    return p1, v1, h1, p2, v2, h2

# Entrada de datos proporcionada por el usuario
p1 = float(input("Ingrese la presión en el punto 1 (Pa): "))
v1 = float(input("Ingrese la velocidad en el punto 1 (m/s): "))
h1 = float(input("Ingrese la altura en el punto 1 (m): "))
p2 = float(input("Ingrese la presión en el punto 2 (Pa): "))
v2 = float(input("Ingrese la velocidad en el punto 2 (m/s): "))
h2 = float(input("Ingrese la altura en el punto 2 (m): "))
rho = float(input("Ingrese la densidad del fluido (kg/m^3): "))
g = float(input("Ingrese la aceleración debida a la gravedad (m/s^2): "))

# Resolución de la ecuación de Bernoulli
p1, v1, h1, p2, v2, h2 = ecuacion_bernoulli(p1, v1, h1, p2, v2, h2)

# Imprimir los resultados
print("Resultados:")
print("Presión en el punto 1:", p1, "Pa")
print("Velocidad en el punto 1:", v1, "m/s")
print("Altura en el punto 1:", h1, "m")
print("Presión en el punto 2:", p2, "Pa")
print("Velocidad en el punto 2:", v2, "m/s")
print("Altura en el punto 2:", h2, "m")