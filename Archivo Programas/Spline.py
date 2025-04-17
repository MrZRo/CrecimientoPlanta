import numpy as np

# Datos del crecimiento de la Palmera Cocotera (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([5, 12, 30, 46, 60, 74, 91])  # Altura en cm
# -------------------------
# Datos del crecimiento del Arbol de la Princesa (Días vs Altura en cm)
#x = np.array([30,60,90,120,150,180])  # Días
#y = np.array([50,100,150,200,250,300])  # Altura en cm
# -------------------------
# Datos del crecimiento del tulipan (Días vs Altura en cm)
x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
y = np.array([5.2, 15.8, 32.5, 48.7, 58.2, 62.1, 62.5])  # Altura en cm
# -------------------------
# Datos del crecimiento del Diente de Leon (Días vs Altura en cm)
#x = np.array([7, 21, 35, 49, 63, 77, 91])  # Días
#y = np.array([2.5,6.8,12.3,18.7,25.0,30.2,35.2])  # Altura en cm

n = len(x) - 1
h = np.diff(x)
alpha = np.zeros(n)

# Paso 1: Calcular alpha
for i in range(1, n):
    alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])

# Paso 2: Resolver el sistema tridiagonal
l = np.ones(n+1)
mu = np.zeros(n)
z = np.zeros(n+1)
c = np.zeros(n+1)
b = np.zeros(n)
d = np.zeros(n)

for i in range(1, n):
    l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
    mu[i] = h[i]/l[i]
    z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

# Paso 3: Sustitución hacia atrás
for j in range(n-1, -1, -1):
    c[j] = z[j] - mu[j]*c[j+1]
    b[j] = (y[j+1] - y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
    d[j] = (c[j+1] - c[j]) / (3*h[j])

# Paso 4: Evaluar en dia objetivo
x_val = 40

# Buscar el intervalo donde está x_val
for i in range(n):
    if x[i] <= x_val <= x[i+1]:
        break

dx = x_val - x[i]
result = y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3


print(f"Spline, valor interpolado en {x_val} días: {result:,.3f}")
