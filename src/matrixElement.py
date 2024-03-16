import numpy as np
from numpy import cos, sin, pi, exp
from src.classes.params import Shiba
from src.classes.lattice import Lattice
from src.decomposition import decompose


def get_A(shib: Shiba, phase: float, R: float) -> complex:
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
    print("A:", matrix)
    return matrix


def get_B(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for spin flip pair creation
    We set Delta (superconducting gap = 1)
    """
    alpha = shib.alpha
    beta = shib.beta
    xi = shib.xi
    delta = shib.delta
    matrix = 8 * beta * alpha**2 / (1 + alpha**2) ** (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * cos(2 * pi * R) * sin(delta)
        + 1j * sin(phase) * sin(2 * pi * R) * cos(delta)
    )
    print("B:", matrix)
    return matrix


def get_C(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for Ising hopping
    """
    alpha = shib.alpha
    xi = shib.xi
    delta = shib.delta
    matrix = -4 * alpha**2 / (1 + alpha**2) ** (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * sin(2 * pi * R) * cos(delta)
        + 1j * sin(phase) * cos(2 * pi * R) * sin(delta)
    )
    print("C:", matrix)
    return matrix


def get_D(shib: Shiba, phase: float, R: float) -> complex:
    """
    Matrix element for spin flipe hopping
    """
    alpha = shib.alpha
    beta = shib.beta
    xi = shib.xi
    delta = shib.delta
    matrix = 8 * beta * alpha**2 / (1 + alpha**2) ** (3 / 2)
    matrix = matrix * exp(-R / xi) / 2 / np.pi / R
    matrix = matrix * (
        cos(phase) * sin(2 * pi * R) * cos(delta)
        + 1j * sin(phase) * cos(2 * pi * R) * sin(delta)
    )
    print("D:", matrix)
    return matrix


def cc(number: complex) -> complex:
    return np.conj(number)


def hc(matrix: np.ndarray) -> np.ndarray:
    return np.conj(matrix).T


def destroy(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from spin conserving terms
    This matrix destroys quasiparticle at the first and second positon
    of the Paulio string index ( coord2, * , coord1)
    """
    R = lat.distance(coord1, coord2)
    phase = lat.phase(shiba.B, coord1, coord2)
    Aij = get_A(shiba, phase, R)
    Bij = get_B(shiba, phase, R)
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


def create(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from spin-flipping terms
    This matrix create quasiparticle at the first and second positon
    of the Pauli string index (coord1, coord2, *)
    """
    R = lat.distance(coord1, coord2)
    phase = lat.phase(shiba.B, coord1, coord2)
    Aij = get_A(shiba, phase, R)
    Bij = get_B(shiba, phase, R)
    return hc(
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [-Bij, 0, -Aij, 0, 0, 0, -cc(Bij), 0],
                [0, -Bij, 0, -Aij, 0, 0, 0, -cc(Bij)],
                [cc(Bij), 0, 0, 0, Aij, 0, Bij, 0],
                [0, cc(Bij), 0, 0, 0, Aij, 0, Bij],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
    )


def hop(
    shiba: Shiba,
    lat: Lattice,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> np.ndarray:
    """
    Transfer matrix between subgap states from pairing term
    The YSR quasiparticle hop from the second to the third index.
    ( occupied , coord1, *) -> (occupied , *, coord2)
    """
    R = lat.distance(coord1, coord2)
    phase = lat.phase(shiba.B, coord1, coord2)
    Cij = get_C(shiba, phase, R)
    Dij = get_D(shiba, phase, R)
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
    lat: Lattice,
    shib: Shiba,
    coord1: np.ndarray,
    coord2: np.ndarray,
) -> dict[tuple, float]:
    """
    Return the table of all coupling arising from second order perturbation theory.
    We use Pauli operator as our basis.
    Spin at the third index does not participate in the interaction.
    """
    matrix = create(shib, lat, coord1, coord2)
    return decompose(hc(matrix) @ matrix)


def thirdOrder(
    lat: Lattice,
    shib: Shiba,
    coord1: np.ndarray,
    coord2: np.ndarray,
    coord3: np.ndarray,
) -> dict[tuple, float]:
    """
    Return the table of all coupling arising from third order perturbation theory.
    We use Pauli string (i,j,k) which cooresponds to position (coord1, coord2, coord3)
    as our basis
    """
    matrix1 = create(shib, lat, coord1, coord2)
    matrix2 = hop(shib, lat, coord2, coord3)
    matrix3 = destroy(shib, lat, coord3, coord1)
    operator1 = matrix3 @ matrix2 @ matrix1
    operator2 = U() @ operator1 @ U().T
    operator3 = U() @ operator2 @ U().T
    return decompose(
        operator1
        + operator2
        + operator3
        + hc(operator1)
        + hc(operator2)
        + hc(operator3)
    )
    # matrix1 = create(shib, lat, coord1, coord2)
    # matrix2 = hop(shib, lat, coord2, coord3)
    # matrix3 = destroy(shib, lat, coord3, coord1)
    # operator1 = matrix3 @ matrix2 @ matrix1
    # return decompose(operator1 + hc(operator1))
