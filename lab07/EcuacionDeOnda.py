import numpy as np
import matplotlib.pyplot as plt

def wave_equation_solver(x0, xn, t0, tn, dx, dt, c, initial_condition, boundary_condition):
    # Número de pasos espaciales y temporales
    nx = int((xn - x0) / dx) + 1
    nt = int((tn - t0) / dt) + 1

    # Parámetro de propagación
    r = (c * dt / dx)**2

    # Crear matrices para almacenar los resultados
    u = np.zeros((nt, nx))

    # Establecer condiciones iniciales
    u[0, :] = initial_condition(np.linspace(x0, xn, nx))

    # Aplicar condiciones de contorno
    u[:, 0] = boundary_condition(t0 + np.linspace(0, tn - t0, nt))
    u[:, -1] = boundary_condition(t0 + np.linspace(0, tn - t0, nt))

    # Resolver la ecuación de onda utilizando diferencias finitas
    for j in range(0, nt - 1):
        for i in range(1, nx - 1):
            u[j+1, i] = 2*(1 - r)*u[j, i] + r*(u[j, i+1] + u[j, i-1]) - u[j-1, i]

    return u

def initial_condition(x):
    return np.sin(2*np.pi*x)

def boundary_condition(t):
    return np.sin(4*np.pi*t) + 1

# Parámetros del problema
x0 = 0.0
xn = 1.0
t0 = 0.0
tn = 0.1
dx = 0.01
dt = 0.0001
c = 1.0

# Resolver la ecuación de onda
u = wave_equation_solver(x0, xn, t0, tn, dx, dt, c, initial_condition, boundary_condition)

# Graficar resultados
x = np.linspace(x0, xn, int((xn - x0) / dx) + 1)
t = np.linspace(t0, tn, int((tn - t0) / dt) + 1)

X, T = np.meshgrid(x, t)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u')
ax.set_title('Solución de la ecuación de onda')
plt.show()
