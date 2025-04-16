import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import numpy as np

# Método SOR
def metodo_sor(A, b, omega, tol, max_iter):
    n = len(b)
    x = np.zeros(n)
    iteraciones = []

    for k in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            suma1 = sum(A[i][j] * x_new[j] for j in range(i))
            suma2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - suma1 - suma2)

        error = np.linalg.norm(x_new - x, ord=np.inf)
        iteraciones.append((k + 1, x_new.copy(), error))

        if error < tol:
            break
        x = x_new

    return x, iteraciones

# Función para recoger y procesar datos
def resolver():
    try:
        n = int(entry_n.get())
        omega = float(entry_omega.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        A = []
        b = []

        for i in range(n):
            fila = []
            for j in range(n):
                valor = float(entries_A[i][j].get())
                fila.append(valor)
            A.append(fila)
            b.append(float(entries_b[i].get()))

        A = np.array(A)
        b = np.array(b)

        resultado, iteraciones = metodo_sor(A, b, omega, tol, max_iter)

        text_result.delete(1.0, tk.END)
        for k, xk, err in iteraciones:
            text_result.insert(tk.END, f"Iteración {k}: x = {xk}, error = {err:.6e}\n")
        text_result.insert(tk.END, f"\nResultado final: x = {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Crear interfaz
root = tk.Tk()
root.title("Método SOR - Sistema de ecuaciones")

tk.Label(root, text="Tamaño de la matriz (n):").grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Label(root, text="ω (factor de relajación):").grid(row=1, column=0)
entry_omega = tk.Entry(root)
entry_omega.grid(row=1, column=1)

tk.Label(root, text="Tolerancia (ε):").grid(row=2, column=0)
entry_tol = tk.Entry(root)
entry_tol.grid(row=2, column=1)

tk.Label(root, text="Máx. iteraciones:").grid(row=3, column=0)
entry_max_iter = tk.Entry(root)
entry_max_iter.grid(row=3, column=1)

def crear_campos():
    global entries_A, entries_b
    try:
        for widget in frame_inputs.winfo_children():
            widget.destroy()
        n = int(entry_n.get())
        entries_A = [[tk.Entry(frame_inputs, width=5) for _ in range(n)] for _ in range(n)]
        entries_b = [tk.Entry(frame_inputs, width=5) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                entries_A[i][j].grid(row=i, column=j)
            tk.Label(frame_inputs, text="|").grid(row=i, column=n)
            entries_b[i].grid(row=i, column=n + 1)

    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido para n.")

tk.Button(root, text="Crear matriz", command=crear_campos).grid(row=0, column=2, padx=5)
tk.Button(root, text="Resolver", command=resolver).grid(row=1, column=2, padx=5)

frame_inputs = tk.Frame(root)
frame_inputs.grid(row=4, column=0, columnspan=3, pady=10)

text_result = scrolledtext.ScrolledText(root, width=70, height=20)
text_result.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
