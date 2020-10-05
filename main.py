import numpy as np
import matplotlib.pyplot as plt


class centroide:
    def __init__(self, ctrd):
        self.ctrd = ctrd
        self.cluster = []

    def add(self, pto):
        self.cluster.append(pto)


def crear_datos(n, d, k):
    """ n: cantidad de vectores
        d: dimension de los vectores
        k: cantidad de centroides
    """
    # puntosi = np.random.randint(1, 10, (10, 2))
    puntos = np.random.rand(n, d)
    centroides = np.random.rand(k, d)

    return puntos, centroides


def calc_dist(pto, ctrd):
    """ calcula la distancia entre dos vectores.
        pto: vector que pertenece al dataset
        ctrd: centroide del cluster
    """
    aux = 0

    # distancia euclidea del punto al centroide
    for i in pto-ctrd:
        aux += i**2

    aux = np.sqrt(aux)

    return aux


def asignar(ptos, ctrds):

    mat = []  # Se crea una lista copia de los centroides
    labels = []

    # En la pos 0 de mat estan los puntos mas cercanos al centroide 0, en la pos 1 al centroide 1 y asi...
    for i in range(len(ctrds)):
        mat.append([])

    # distancia de cada uno de los puntos a todos los centroides
    for pto in ptos:
        distancias = []     # guarda las distancias de pto a cada uno de los ctrds
        for ctrd in ctrds:
            dist = calc_dist(pto, ctrd)
            distancias.append(dist)

        dist_min = min(distancias)
        dist_min_indice = distancias.index(dist_min)
        # nearest = ctrds[dist_min_indice]
        # labels.append(dist_min_indice)
        mat[dist_min_indice].append(pto.tolist())

    return mat


def clusters(ptos, ctrds):

    while True:
        new_ctrds = []

        mat = asignar(ptos, ctrds)

        for i in range(len(ctrds)):
            new_ctrds.append(np.array(mat[i]).mean(0))

        if np.all(ctrds == new_ctrds):
            break

        ctrds = new_ctrds  # copy?

    return ctrds


# print(puntosf)
# print(calc_dist(puntosi[0], puntosi[3]))
puntosi, centroides = crear_datos(10, 2, 3)

clusters = clusters(puntosi, centroides)

# fig = plt.scatter(puntosi[:, 0], puntosi[:, 1])
# plt.show()


if __name__ == '__main__':
    print('PyCharm')

