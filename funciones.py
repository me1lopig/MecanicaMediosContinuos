# funciones para aplicar a tensores


# Lista de funciones
# invariantes, calcula los invariantes de un tensor
# eigen, calcula los autovalores y los autovectores de un tensor
# esf_desv, calcula los tensones esfericos y desviadores de una tensor
# 
# def_elastica, calcula el tensor de deformacion


# importacion de librerias 
import numpy as np


# definición de funciones

def invariantes(tensor):

    # Calcular las autovalores del tensor
    autovalores = np.linalg.eigvals(tensor)

    # Calcular las invariantes
    I1 = np.sum(autovalores)
    I2 = np.prod(autovalores)
    I3 = np.linalg.det(tensor)

    return I1,I2,I3



def eigen(tensor):
    # Calcular los autovalores y autovectores de un tensor
    autovalores, autovectores = np.linalg.eig(tensor)
    return autovalores,autovectores



def esf_desv(tensor):
    # Calcular las autovalores del tensor
    autovalores = np.linalg.eigvals(tensor)

    # Calcular la media de los autovalores
    media = np.mean(autovalores)

    # Crear la matriz identidad
    I = np.identity(len(tensor))

    # Calcular el tensor esférico
    tensor_esferico = media * I

    # Calcular el tensor desviador
    tensor_desviador = tensor - tensor_esferico

    return tensor_esferico,tensor_desviador