import numpy as np

# Datos del crecimiento de la Palmera Cocotera (Días vs Altura en cm)
x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
y = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento del Arbol de la Princesa (Días vs Altura en cm)
#x = np.array([30,60,90,120,150,180])  # Días
#y = np.array([50,100,150,200,250,300])  # Altura en cm
# -------------------------
# Datos del crecimiento del tulipan (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([5.2, 15.8, 32.5, 48.7, 58.2, 62.1, 62.5])  # Altura en cm
# -------------------------
# Datos del crecimiento del Diente de Leon (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([2.5,6.8,12.3,18.7,25.0,30.2,35.2])  # Altura en cm

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
