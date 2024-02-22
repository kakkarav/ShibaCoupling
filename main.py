import numpy as np


class Shiba:
    def __init__(self, alpha, beta, lambdaF, xi):
        self.alpha = alpha
        self.beta = beta
        self.xi = xi / lambdaF

    def Energy(self, alpha):
        return (1 - alpha**2) / (1 + alpha**2)

    def theta(self, alpha):
        return np.arctan(alpha)

    def N(self):
        pass

    def SecondXX(self):
        pass

    def SecondZZ(self):
        pass

    def ThirdXX(self):
        pass

    def ThirdXYZ(self):
        pass

    def thirdChiral(self):
        pass
