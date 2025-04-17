import numpy as np

# Datos del crecimiento de la Palmera Cocotera (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento del Arbol de la Princesa (Días vs Altura en cm)
x = np.array([30,60,90,120,150,180])  # Días
y = np.array([50,100,150,200,250,300])  # Altura en cm
# -------------------------
# Datos del crecimiento del tulipan (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([5.2, 15.8, 32.5, 48.7, 58.2, 62.1, 62.5])  # Altura en cm
# -------------------------
# Datos del crecimiento del Diente de Leon (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([2.5,6.8,12.3,18.7,25.0,30.2,35.2])  # Altura en cm
# -------------------------
# FUNCION DE LAGRANGE
# -------------------------

def lagrange_interpolation(x_data, y_data, x):
    """
    Calcula la interpolación de Lagrange para un punto x
    dados los vectores x_data e y_data.
    """
    total = 0
    n = len(x_data)

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        total += term
    return total

# -------------------------
# EJECUCIÓN
# -------------------------

# Calcular la altura estimada para el día 69
dia_objetivo = 111
altura_estimacion_lagrange = lagrange_interpolation(x_days, y_height_cm, dia_objetivo)

print(f"Altura estimada de la palmera en el día {dia_objetivo} (Lagrange): {altura_estimacion_lagrange:.2f} cm")
