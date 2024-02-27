from .classes import params, lattice
from . import matrixElement as me


class Coupling:
    def __init__(self, vec1, vec2, N, R, alpha, beta, lambdaF, xi, B):
        self.lat = lattice.Lattice(vec1, vec2, N, R)
        self.shiba = params.Shiba(alpha, beta, lambdaF, xi, B)

    def coupling(self):
        return me.U


def test():
    return params.Shiba(1, 1, 1, 1, 1)
