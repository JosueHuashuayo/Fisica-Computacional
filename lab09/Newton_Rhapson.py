import math as ma
def newton_raphson_recursive(f, f_prime, x, tolerance):
    """
    Método de Newton-Raphson recursivo para encontrar una raíz de una función.
    Args:
        f: La función para la cual se desea encontrar la raíz.
        f_prime: La derivada de la función f.
        x: El punto actual de la iteración.
        tolerance: La tolerancia para considerar que se ha encontrado una raíz.
    """
    if abs(f(x)) <= tolerance :
        return x
    
    x_next = x - f(x) / f_prime(x)
    
    return newton_raphson_recursive(f, f_prime, x_next, tolerance)

def f(x):
    return x**3 + 4*x**2 - 10

def f_prime(x):
    return 3*x**2 + 8*x

root = newton_raphson_recursive(f, f_prime, 0.1 ,0.000001)

print("Raíz encontrada:", root)