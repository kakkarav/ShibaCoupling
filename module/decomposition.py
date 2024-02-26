import numpy as np
import itertools

pauli = {}
pauli[0] = np.eye(2)
pauli[1] = np.array([[0, 1], [1, 0]])
pauli[2] = np.array([[0, -1j], [1j, 0]])
pauli[3] = np.array([[1, 0], [0, -1]])


def decompose(Matrix: np.ndarray) -> dict:
    """
    Decompose a matrix into its Pauli components
    """
    table = {}
    dim = np.log2(len(Matrix))
    digits = list(range(4))
    AllIndices = itertools.product(digits, repeat=dim)
    for index in AllIndices:
        operator = np.array([1])
        for i in range(dim):
            operator = np.kron(operator, pauli[index[i]])
        table[index] = np.dot(operator, Matrix).trace()
    return table
