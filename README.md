# Análisis Numérico del Crecimiento de Plantas 🌱📊

![Badge en desarrollo](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/Licencia-MIT-green)

Este repositorio contiene los códigos, hojas de cálculo y resultados obtenidos al modelar y predecir el crecimiento de plantas en distintos días usando métodos numéricos como:
- Método de Newton (interpolación por diferencias divididas)
- Interpolación de Lagrange
- Interpolación por Spline cúbico
- Regresión lineal


## 📌 Integrantes
* Aguilar Morejón Camila Madeleine (Paulownia tomentosa)
* Aruquipa Coca Jose Andres (Diente de León)
* Zabala Lazo Evians Reyna (Tulipan)
* Zeballos Romero Daniel Alfredo (La Palmera Cocotera)


## 📌 Tabla de Contenidos
- [Objetivos](#objetivos)
- [Metodología](#metodología)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Herramientas Utilizadas](#herramientas-utilizadas)
- [Resultados Preliminares](#resultados-preliminares)
- [Cómo Usar este Repositorio](#cómo-usar-este-repositorio)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Referencias](#referencias)

## 🎯 Objetivos
1. Modelar matemáticamente el crecimiento de plantas usando ecuaciones diferenciales.
2. Implementar algoritmos numéricos (ej. regresión lineal, métodos Newton, Splime y Lagrange) en Python.
3. Analizar datos experimentales (dias y crecimiento de cm.) almacenados en Excel.
4. Evaluar y comparar la precisión de distintos métodos numéricos para estimar el crecimiento de diferentes plantas en días intermedios a partir de datos reales o simulados.
5. Dar un analisis en un informe.

## ![enter image description here](https://img.icons8.com/?size=40&id=c2AXPLZ3iVEU&format=png&color=000000)Rutas
.
├── data/                   # Datos brutos y procesados
│   ├── raw/               │   │   ├── experimento_1.xlsx
│   │   └── experimento_2.xlsx
│   └── processed/         # Datos limpios para análisis
│       └── datos_filtrados.csv
├── notebooks/             # Jupyter/Colab notebooks
│   └── analisis_exploratorio.ipynb
├── src/                   # Código Python
│   ├── modelos/          │   │   ├── euler_method.py
│   │   └── regresion_polinomial.py
│   └── visualizacion/
│       └── graficos_matplotlib.py
├── docs/                  # Documentación adicional
│   └── referencias.pdf
└── README.md              # Este archivo

## 📊 Metodología
```mermaid
graph TD
    A[Datos Experimentales] --> B(Preprocesamiento en Pandas)
    B --> C[Modelado Matemático]
    C --> D{Análisis Numérico}
    D --> E[Visualización]
    D --> F[Predicciones]
