# aplicación de Python a la Mecánica de los Médios Contínuos
# version 05/02/2023
# Germán López Pineda
# Ingeniero de Caminos Canales y Puertos UGR
# Master en Matemática Computacional UJI
# Master en Ingeniería del Terreno UCO
# Grupo de investigación RNM 244 Ingeniería Ambiental y Geofísica Universidad de Córdoba

import funciones as fn

# introducción de las componentes del tensor
t11=20
t22=10
t33=100
t12=0
t13=25
t23=0
# composicion del tensor
tensor=([t11,t12,t13],[t12,t22,t23],[t13,t23,t33])

# impresion del tensor
print('El tensor es ')
print(tensor)

# invariantes
I1,I2,I3=fn.invariantes(tensor)
print('Los invariantes del tensor son ')
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