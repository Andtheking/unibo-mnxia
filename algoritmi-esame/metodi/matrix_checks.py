import numpy as np


def matrix_checks(matrix: np.matrix):
    """_Stampa le informazioni per capire quale algoritmo utilizzare per risolvere un sistema del tipo Ax = b_

    Args:
        matrix (np.matrix): _Matrice da controllare_
    """
    print("Dimensioni matrice: ", matrix.shape)
    print("Simmetrica? ", np.allclose(matrix, matrix.T)) # Per essere simmetrica la trasposta deve essere uguale all'originale
    print("Definita positiva? ", np.all(np.linalg.eigvals(matrix) > 0)) # Per essere definita positiva tutti gli autovalori devono essere positivi
    print("Condizionamento: ", np.linalg.cond(matrix))
    print("Rango: ", np.linalg.matrix_rank(matrix))


if __name__ == '__main__':
    A = np.random.rand(100, 200)
    matrix_checks(A)

