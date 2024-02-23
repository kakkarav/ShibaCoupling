import numpy as np

from module.main import Shiba


def energy(alpha: float) -> float:
    return (1 - alpha**2) / (1 + alpha**2)


# Phase shift from disorder scattering
def phaseShift(alpha):
    return np.arctan(alpha)


# Normalzing factor for second order perturabation
def N2(shib: Shiba, R: float) -> float:
    return 0.0


# Normalzing factor for third order perturbation
def N3(
    sehib: Shiba,
    R1: float,
    R2: float,
    R3: float,
) -> float:
    return 1.0
