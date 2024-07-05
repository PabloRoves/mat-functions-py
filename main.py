"""Pruebas de funciones"""
import lineal as Lineal
from cuadratica import Cuadratica
import parabola as Parabola

# Funciones lineales
# ----------------------
# Lineal.funcion_lineal()


# Funciones cuadratica
# ---------------------
print("Ingresa los coeficientes")
ca = int(input())
cb = int(input())
cc = int(input())

cuadratica1 = Cuadratica(ca, cb, cc)
print(cuadratica1.obtener_raices())
print(cuadratica1.expresion_general())
cuadratica1.graficar()
# cuadratica2 = Cuadratica()

# ECUACION2 = cuadratica2.expresion_general(ca, cb, cc)
# print(ECUACION2)

# A = -20
# B = 10
# C = 20

# print(Cuadratica.mostrarEcuacion(A, B, C))
# print(Cuadratica.obtenerX(A, B, C))
# Cuadratica.graficar(A, B, C)

# Parabolas
# ----------

# Parabola.funcion_parabola()
