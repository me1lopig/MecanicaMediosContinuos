

import numpy as np

# Define el tensor de tensiones
tensor = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calcular las autovalores del tensor
autovalores = np.linalg.eigvals(tensor)

# Calcular las invariantes
I1 = np.sum(autovalores)
I2 = np.prod(autovalores)
I3 = np.linalg.det(tensor)

# Imprimir los resultados
print("Primera invariante (I1):", I1)
print("Segunda invariante (I2):", I2)
print("Tercera invariante (I3):", I3)
