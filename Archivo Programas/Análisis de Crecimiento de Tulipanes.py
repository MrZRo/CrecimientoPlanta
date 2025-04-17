Código Python para Análisis de Crecimiento de Tulipanes con los metodos, newton, lagrange, spline y regresion lineal 🌷

import numpy as np
from scipy.interpolate import lagrange, CubicSpline
from scipy import stats
import matplotlib.pyplot as plt

# Datos de crecimiento de tulipanes (días vs altura en cm)
dias = np.array([7, 21, 35, 49, 63, 77, 91])
alturas = np.array([5.2, 15.8, 32.5, 48.7, 58.2, 62.1, 62.5])

# Día a interpolar
dia_interpolar = 40

## 1. Método de Newton (Diferencias Divididas)
def newton_interpolation(x, y, x_eval):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j] - x[i])
    
    resultado = coef[0,0]
    producto = 1.0
    for j in range(1,n):
        producto *= (x_eval - x[j-1])
        resultado += coef[0,j] * producto
    
    return resultado

newton_result = newton_interpolation(dias, alturas, dia_interpolar)

## 2. Método de Lagrange
def lagrange_interpolation(x, y, x_eval):
    poly = lagrange(x, y)
    return poly(x_eval)

lagrange_result = lagrange_interpolation(dias, alturas, dia_interpolar)

## 3. Splines Cúbicos
def spline_interpolation(x, y, x_eval):
    cs = CubicSpline(x, y, bc_type='natural')
    return cs(x_eval)

spline_result = spline_interpolation(dias, alturas, dia_interpolar)

## 4. Regresión Lineal
def linear_regression(x, y, x_eval):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return intercept + slope * x_eval

linear_result = linear_regression(dias, alturas, dia_interpolar)

## Resultados
print(f"Resultados para día {dia_interpolar}:")
print(f"- Newton: {newton_result:.2f} cm")
print(f"- Lagrange: {lagrange_result:.2f} cm")
print(f"- Spline Cúbico: {spline_result:.2f} cm")
print(f"- Regresión Lineal: {linear_result:.2f} cm")

## Gráfico comparativo
plt.figure(figsize=(10, 6))
plt.scatter(dias, alturas, color='red', label='Datos reales', zorder=5)

# Newton (evaluamos en varios puntos para graficar)
x_newton = np.linspace(min(dias), max(dias), 100)
y_newton = [newton_interpolation(dias, alturas, xi) for xi in x_newton]
plt.plot(x_newton, y_newton, '--', label='Newton', alpha=0.7)

# Lagrange
x_lagrange = np.linspace(min(dias), max(dias), 100)
y_lagrange = [lagrange_interpolation(dias, alturas, xi) for xi in x_lagrange]
plt.plot(x_lagrange, y_lagrange, ':', label='Lagrange', alpha=0.7)

# Spline
x_spline = np.linspace(min(dias), max(dias), 100)
y_spline = spline_interpolation(dias, alturas, x_spline)
plt.plot(x_spline, y_spline, '-', label='Spline Cúbico', linewidth=2)

# Regresión Lineal
x_linear = np.array([min(dias), max(dias)])
y_linear = linear_regression(dias, alturas, x_linear)
plt.plot(x_linear, y_linear, '-.', label='Regresión Lineal')

plt.title('Comparación de Métodos de Interpolación - Crecimiento de Tulipanes')
plt.xlabel('Días')
plt.ylabel('Altura (cm)')
plt.legend()
plt.grid(True)
plt.show()
