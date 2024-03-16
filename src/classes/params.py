import numpy as np
from dataclasses import dataclass


# the classical shiba energy in the unit of superconducting gap
def energy(alpha: float) -> float:
    return (1 - alpha**2) / (1 + alpha**2)


# Phase shift from disorder scattering
# alpha
def phaseShift(alpha):
    return np.arctan(alpha)


@dataclass
class Params:
    # The unit vectors in the Cartesian coordinate
    vec1: np.ndarray
    vec2: np.ndarray
    # The lattice spacing in meter
    R: float
    # The dimensionless exchange coupling
    alpha: float
    # The small perturbative parameter for the spin flip term
    beta: float
    # Fermi wavelength in meter
    lambda_F: float
    # Superconductor coherence length in meter
    xi: float
    # Magnetic field in Tesla
    B: float


# All the energy scales are in the unit of the supercoducting gap
# Note R is assumed to be in the unit of lambdaF
# Here we need to assume about some parameter
class Shiba:
    def __init__(self, params: Params):
        self.alpha = params.alpha
        self.beta = params.beta
        self.xi = params.xi / params.lambda_F
        self.energy = energy(params.alpha)
        self.delta = phaseShift(params.alpha)
        self.B = params.B

    def __repr__(self):
        ans = ""
        for key, value in self.__dict__.items():
            ans += f"{key} : {value} \n"
        return ans
