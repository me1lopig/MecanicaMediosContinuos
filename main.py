# aplicación de Python a la Mecánica de los Médios Contínuos
# version 05/02/2023
# Germán López Pineda
# Ingeniero de Caminos Canales y Puertos UGR
# Master en Matemática Computacional UJI
# Master en Ingeniería del Terreno UCO
# Grupo de investigación RNM 244 Ingeniería Ambiental y Geofísica Universidad de Córdoba

import funciones as fn

# introducción del tensor 
tensor=([20,0,25],[0,10,0],[25,0,100])

# invariantes
I1,I2,I3=fn.invariantes(tensor)
print(I1," ",I2," ",I3)

# autovalores y autovectores
autovalores,autovectores=fn.eigen(tensor)
print('autovalores')
print(autovalores)
print('autovectores')
print(autovectores)

# tensor esferico y desviador
esferico,desviador=fn.esf_desv(tensor)
print('Tensor esferico')
print(esferico)
print('Tensor desviador')
print(desviador)