import numpy as np
from . import helper


# Note R is assumed to be in the unit of lambdaF
# Here we need to assume about some parameter
class Shiba:
    def __init__(self, alpha, beta, lambdaF, xi, Bfield):
        self.alpha = alpha
        self.beta = beta
        self.xi = xi / lambdaF
        self.energy = helper.energy(alpha)
        self.B = Bfield

    def SecondXX(self, R):
        pass

    def SecondZZ(self, R):
        pass

    def ThirdXX(self, R1, R2, R3):
        pass

    def ThirdXYZ(self, R1, R2, R3):
        pass

    def thirdChiral(self, R1, R2, R3):
        pass
