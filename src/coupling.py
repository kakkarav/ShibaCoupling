from module.classes import params, lattice
from module import matrixElement as me


class Coupling:
    def __init__(
        self,
    ):
        self.lat = lattice.Lattice(1, 1, 1, 1)
        self.shiba = params.Shiba(1, 1, 1, 1, 1, 1, 1)

    def coupling(self):
        return me.U


def test():
    return params.Shiba(1, 1, 1, 1, 1, 1, 1)
