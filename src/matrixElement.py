import numpy as np
from numpy import cos, sin, pi, exp
from src.classes.params import Shiba
from src.classes.lattice import Lattice


def A(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for Ising pair creation ( initial state is the ket)
    We set Delta (superconducting gap = 1)
    """
    alpha = shib.alpha
    xi = shib.xi
    delta = shib.delta
    matrix = -4 * alpha**2 / (1 + alpha**2) ** (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * cos(phase) * cos(2 * pi * R) * sin(delta)
    return matrix


def B(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for spin flip pair creation
    We set Delta (superconducting gap = 1)
    """
    alpha = shib.alpha
    beta = shib.beta
    xi = shib.xi
    delta = shib.delta
    matrix = 8 * beta * alpha**2 / (1 + alpha**2) ^ (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * cos(2 * pi * R) * sin(delta)
        + 1j * sin(phase) * sin(2 * pi * R) * cos(delta)
    )
    return matrix


def C(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for Ising hopping
    """
    alpha = shib.alpha
    xi = shib.xi
    delta = shib.delta
    matrix = -4 * alpha**2 / (1 + alpha**2) ^ (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * sin(2 * pi * R) * cos(delta)
        + 1j * sin(phase) * cos(2 * pi * R) * sin(delta)
    )
    return matrix


def D(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for spin flipe hopping
    """
    alpha = shib.alpha
    beta = shib.beta
    xi = shib.xi
    delta = shib.delta
    matrix = 8 * beta * alpha**2 / (1 + alpha**2) ^ (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * sin(2 * pi * R) * cos(delta)
        + 1j * sin(phase) * cos(2 * pi * R) * sin(delta)
    )
    return matrix


def cc(number: complex) -> complex:
    return np.conj(number)


def M1(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from spin conserving terms
    """
    R = lat.distance(coord1, coord2)
    phase = 1
    Aij = A(shiba, phase, R)
    Bij = B(shiba, phase, R)
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


def M2(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from spin-flipping terms
    """
    R = lat.distance(coord1, coord2)
    phase = 1
    Aij = A(shiba, phase, R)
    Bij = B(shiba, phase, R)
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


def M3(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from pairing term
    """
    R = lat.distance(coord1, coord2)
    phase = 1
    Cij = C(shiba, phase, R)
    Dij = D(shiba, phase, R)
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
    """
    Permutation matrix that permute the indices cyclically
    """
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


def secondOrder(
    shib: Shiba, coord1: np.ndarray, coord2: np.ndarray
) -> dict[tuple, float]:
    """
    Return the table of all coupling arising from second order perturbation theory
    """
    return {}


def ThirdOrder(
    shib: Shiba, coord1: np.ndarray, coord2: np.ndarray, coord3: np.ndarray
) -> dict[tuple, float]:
    """
    Return the table of all coupling arising from third order perturbation theory
    """
    return {}
