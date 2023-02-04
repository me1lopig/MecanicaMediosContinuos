# libreria para el uso en MMC
# programa para calcular autovalores y autovectores
# para aplicar en tensores de tensiones y deformaciones

# listado de funciones


import numpy as np

# Define el tensor de tensiones
tensor = np.array([[1, 4, 3], [4, 5, 5], [7, 8, 7]])

# Calcular los autovalores y autovectores
autovalores, autovectores = np.linalg.eig(tensor)

# Imprimir los resultados
print("Autovalores:", autovalores)
print("Autovectores:")
print(autovectores)
