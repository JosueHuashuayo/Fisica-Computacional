# import matplotlib.pyplot as plt
# import numpy as np

# def aceleracion(vf,vi,t):
#     return (vf-vi)/t

# x = float(input("Ingrese la distancia(x): "))
# t = float(input("Ingrese el tiempo(t): "))
# m = float(input("Ingrese la masa(m): "))
# vi = float(input("Ingrese la velocidad inicial(m/s): "))
# vf = float(input("Ingrese la velocidad final(m/s): "))

# a = aceleracion(vf, vi, t)
# print("Aceleración:", a, "m/s^2")
# f = m * a
# print("Fuerza:", f, "N")

# plt.plot([0,t],[vi,vf])
# plt.title('Aceleracion')
# plt.xlabel('Tiempo')
# plt.ylabel('Velocidad')
# plt.show()

# Solicitar las masas al usuario
masa_1 = float(input("Ingrese la masa del objeto 1 en kilogramos: "))
masa_2 = float(input("Ingrese la masa del objeto 2 en kilogramos: "))
gravedad = 9.8  # aceleración gravitatoria en metros por segundo al cuadrado

# Calculando la magnitud de la aceleración y la tensión en la cuerda
diferencia_masas = abs(masa_1 - masa_2)  # diferencia de masas en kilogramos
aceleracion = diferencia_masas * gravedad / (masa_1 + masa_2)  # aceleración en metros por segundo al cuadrado
tension_cuerda = masa_1 * aceleracion  # tensión en la cuerda sin peso en newtons

print("Magnitud de la aceleración:", aceleracion, "m/s^2")
print("Tensión en la cuerda sin peso:", tension_cuerda, "N")
