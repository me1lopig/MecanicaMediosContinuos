# funciones para aplicar a tensores


# Lista de funciones
# invariantes, calcula los invariantes de un tensor
# eigen, calcula los autovalores y los autovectores de un tensor
# esf_desv, calcula los tensones esfericos y desviadores de una tensor
# cam_base, cambio de base por giro de loe ejes de referencia
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

def cam_base(alpha,beta,gamma):
    # funcion para la realización de un cambio de base por rotación de los ejes

    # pasamos a radianes
    alpha=np.deg2rad(alpha) # ángulo de rotación alrededor del eje x
    beta=np.deg2rad(beta) # ángulo de rotación alrededor del eje y
    gamma=np.deg2rad(gamma) # ángulo de rotación alrededor del eje z

    # Definir las matrices de rotación correspondientes
    Gx = np.array([[1, 0, 0],
        [0, np.cos(alpha), -np.sin(alpha)],
        [0, np.sin(alpha), np.cos(alpha)]])

    Gy = np.array([[np.cos(beta), 0, np.sin(beta)],
        [0, 1, 0],
        [-np.sin(beta), 0, np.cos(beta)]])

    Gz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
        [np.sin(gamma), np.cos(gamma), 0],
        [0, 0, 1]])

    # Calcular la matriz de cambio de ejes
    G = Gz @ Gy @ Gx

    # salida de la matriz de cambio de base
    return G
