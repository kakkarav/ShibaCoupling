import numpy as np
from module.classes.params import Shiba


# Normalzing factor for second order perturabation
def N2(shib: Shiba, R: float) -> float:
    return 0.0


# Normalzing factor for third order perturbation
def N3(
    shib: Shiba,
    R1: float,
    R2: float,
    R3: float,
) -> float:
    return 1.0


def A(shib: Shiba, i: int, j: int) -> complex:
    return complex(shib.xi, j)


def B(shib: Shiba, i: int, j: int) -> complex:
    return complex(shib.xi, j)


def C(i: int, j: int) -> complex:
    return complex(i, j)


def D(i: int, j: int) -> complex:
    return complex(i, j)


def cc(number: complex) -> complex:
    return np.conj(number)


def M1(shib: Shiba, i, j):
    Aij = A(shib, i, j)
    Bij = B(shib, i, j)
    return np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [cc(Bij), Aij, 0, 0, 0, Bij, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, cc(Bij), Aij, 0, 0, 0, Bij],
            [-Bij, 0, 0, 0, -Aij, -cc(Bij), 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -Bij, 0, 0, 0, -Aij, -cc(Bij)],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )


def M2(shib: Shiba, i, j):
    Aij = A(shib, i, j)
    Bij = B(shib, i, j)
    return np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-Bij, 0, Aij, 0, 0, 0, -cc(Bij), 0],
            [0, -Bij, 0, Aij, 0, 0, 0, -cc(Bij)],
            [cc(Bij), 0, 0, 0, -Aij, 0, Bij, 0],
            [0, cc(Bij), 0, 0, 0, -Aij, 0, Bij],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )


def M3(i, j):
    Cij = C(i, j)
    Dij = D(i, j)
    return np.array(
        [
            [Cij, 0, Dij, 0, 0, 0, 0, 0],
            [Dij, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, Dij, 0, 0, 0, 0],
            [0, Dij, 0, Cij, 0, 0, 0, 0],
            [0, 0, 0, 0, Cij, 0, Dij, 0],
            [0, 0, 0, 0, Dij, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, Dij],
            [0, 0, 0, 0, 0, Dij, 0, Cij],
        ]
    )


def U():
    return np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ]
    )


def SecondXX(R):
    pass


def SecondZZ(R):
    pass


def ThirdXX(R1, R2, R3):
    pass


def ThirdXYZ(R1, R2, R3):
    pass


def thirdChiral(R1, R2, R3):
    pass
