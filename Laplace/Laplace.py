import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
L = 1.0  # Longitud del dominio
N = 10  # Número de términos en la serie de Fourier
M = 100  # Número de puntos en la discretización espacial
dx = 2 * L / M  # Paso de discretización espacial

# Definir función periódica (ejemplo: función seno)
def periodic_function(x):
    return np.sin(np.pi * x / L)

# Calcular coeficientes de Fourier
coefficients_a = np.zeros(N+1)
coefficients_b = np.zeros(N+1)

for n in range(1, N+1):
    sum_a = 0.0
    sum_b = 0.0

    for m in range(M):
        x_m = -L + m * dx
        f_m = periodic_function(x_m)
        sum_a += f_m * np.cos(n * np.pi * x_m / L)
        sum_b += f_m * np.sin(n * np.pi * x_m / L)

    coefficients_a[n] = (2 / L) * sum_a
    coefficients_b[n] = (2 / L) * sum_b

# Calcular solución de la ecuación de Laplace
u = np.zeros(M)

for m in range(M):
    x_m = -L + m * dx
    sum_u = coefficients_a[0] / 2

    for n in range(1, N+1):
        sum_u += coefficients_a[n] * np.cos(n * np.pi * x_m / L) + coefficients_b[n] * np.sin(n * np.pi * x_m / L)

    u[m] = sum_u

# Visualizar solución
x = np.linspace(-L, L, M)
plt.plot(x, u)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Solución de la ecuación de Laplace con series de Fourier')
plt.grid(True)
plt.show()
