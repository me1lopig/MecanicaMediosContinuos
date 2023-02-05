# calculo de los tensores esferico y desviador 


import numpy as np

# Define el tensor de tensiones
tensor = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calcular las autovalores del tensor
autovalores = np.linalg.eigvals(tensor)

# Calcular la media de los autovalores
media = np.mean(autovalores)

# Crear la matriz identidad
I = np.identity(3)

# Calcular el tensor esférico
tensor_esferico = media * I

# Calcular el tensor desviador
tensor_desviador = tensor - tensor_esferico

# Imprimir los resultados
print("Tensor esférico:")
print(tensor_esferico)
print("Tensor desviador:")
print(tensor_desviador)
