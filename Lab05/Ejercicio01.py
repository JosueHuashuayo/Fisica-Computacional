def ecuacion_continuidad(A1, v1, A2, v2):
    if A1 is None:
        A1 = (A2 * v2) / v1
    elif v1 is None:
        v1 = (v2 * A2) / A1
    elif A2 is None:
        A2 = (A1 * v1) / v2
    elif v2 is None:
        v2 = (v1 * A1) / A2
    
    return A1, v1, A2, v2

# Entrada de datos
A1 = float(input("Ingrese el área en el punto 1 (m^2): "))
v1 = float(input("Ingrese la velocidad en el punto 1 (m/s): "))
A2 = float(input("Ingrese el área en el punto 2 (m^2): "))
v2 = float(input("Ingrese la velocidad en el punto 2 (m/s): "))

# Resolución de la ecuación de continuidad
A1, v1, A2, v2 = ecuacion_continuidad(A1, v1, A2, v2)

# Resultados
print("Resultados:")
print("Área en el punto 1:", A1, "m^2")
print("Velocidad en el punto 1:", v1, "m/s")
print("Área en el punto 2:", A2, "m^2")
print("Velocidad en el punto 2:", v2, "m/s")
