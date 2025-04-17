import numpy as np

# Datos del crecimiento de la palmera cocotera (Días vs Altura en cm)
x_days = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
y_height_cm = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm

# -------------------------
# REGRESIÓN LINEAL SIMPLE
# -------------------------

def regresion_lineal(x, y):
    """
    Calcula los coeficientes de la recta de regresión lineal y = a*x + b
    """
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x * x)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return a, b

# Calcular la recta de regresión
a, b = regresion_lineal(x_days, y_height_cm)

# Estimar altura para el día 69
dia_objetivo = 69
altura_estimacion_regresion = a * dia_objetivo + b

print(f"Altura estimada por regresión lineal en el día {dia_objetivo}: {altura_estimacion_regresion:.2f} cm")
