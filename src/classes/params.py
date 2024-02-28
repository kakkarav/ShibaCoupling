import numpy as np


# the classical shiba energy in the unit of superconducting gap
def energy(alpha: float) -> float:
    return (1 - alpha**2) / (1 + alpha**2)


# Phase shift from disorder scattering
# alpha
def phaseShift(alpha):
    return np.arctan(alpha)


# All the energy scales are in the unit of the supercoducting gap
# Note R is assumed to be in the unit of lambdaF
# Here we need to assume about some parameter
class Shiba:
    def __init__(self, alpha, beta, lambdaF, xi, B):
        self.alpha = alpha
        self.beta = beta
        self.xi = xi / lambdaF
        self.energy = energy(alpha)
        self.delta = phaseShift(alpha)
        self.B = B

    def __repr__(self):
        ans = ""
        for key, value in self.__dict__.items():
            ans += f"{key} : {value} \n"
        return ans
