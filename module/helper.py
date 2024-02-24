import numpy as np

from module.main import Shiba


# the classical shiba energy in the unit of superconducting gap
def energy(alpha: float) -> float:
    return (1 - alpha**2) / (1 + alpha**2)


# Phase shift from disorder scattering
# alpha
def phaseShift(alpha):
    return np.arctan(alpha)


def A(lat, coord1, coord2):
    pass


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
