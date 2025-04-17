import numpy as np

# Datos del crecimiento de la palmera cocotera (Días vs Altura en cm)
x_days = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
y_height_cm = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento de la palmera cocotera (Días vs Altura en cm)
#x_days = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y_height_cm = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento de la palmera cocotera (Días vs Altura en cm)
#x_days = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y_height_cm = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento de la palmera cocotera (Días vs Altura en cm)
#x_days = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y_height_cm = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm

# -------------------------
# FUNCIONES DE NEWTON
# -------------------------

def newton_divided_diff(x, y):
    """
    Calcula los coeficientes del polinomio de interpolación de Newton
    usando diferencias divididas.
    """
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])
    return coef

def newton_polynomial(coef, x_data, x):
    """
    Evalúa el polinomio de Newton para un valor x dado.
    """
    n = len(coef)
    p = coef[-1]
    for k in range(n - 2, -1, -1):
        p = p * (x - x_data[k]) + coef[k]
    return p

# -------------------------
# EJECUCIÓN
# -------------------------

# Calcular los coeficientes del polinomio
coef_newton = newton_divided_diff(x_days, y_height_cm)

# Calcular la altura estimada para el día 69
dia_objetivo = 69
altura_estimacion = newton_polynomial(coef_newton, x_days, dia_objetivo)

print(f"Altura estimada de la palmera en el día {dia_objetivo}: {altura_estimacion:.2f} cm")
