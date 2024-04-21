from src.classes import params, lattice
from src import matrix_element as me
from src import matrix_element_approx as mea
import numpy as np


class Coupling:
    def __init__(self, parameters: params.Params):
        self.lat = lattice.Lattice(parameters)
        self.shiba = params.Shiba(parameters)

    def second_order(self, coord1: np.ndarray, coord2: np.ndarray):
        """
        Return a dictionary contain all coupling.
        We will get 2-body interaction but will will also include the third spin for consistency
        """
        return me.total_second_order(self.lat, self.shiba, coord1, coord2)

    def third_order(self, coord1: np.ndarray, coord2: np.ndarray, coord3: np.ndarray):
        """
        Return a dictioanry contain all coupling where the order of the operator index are conserved.
        correspond to the orfer of the coordoinate
        """
        return me.total_third_order(self.lat, self.shiba, coord1, coord2, coord3)

    def second_order_approx(self, distance: float):
        """
        Return a dictionary contain all coupling.
        We will get 2-body interaction but will will also include the third spin for consistency

        R: distance in the unit of Fermi wavelength
        """
        couplings = {}
        couplings[(1, 1)] = mea.second_order_xx(self.shiba, distance)
        couplings[(2, 2)] = mea.second_order_xx(self.shiba, distance)
        couplings[(3, 3)] = mea.second_order_zz(self.shiba, distance)
        return couplings

    def third_order_approx(self, R12: float, R23: float, R31: float):
        """
        Return a dictioanry contain all coupling where the order of the operator index are conserved.
        correspond to the orfer of the coordoinate

        R: distance in the unit of Fermi wavelength
        """
        couplings = {}
        couplings[(1, 1)] = mea.third_order_zz_intermediate(self.shiba, R12, R23, R31)
        couplings[(2, 2)] = mea.third_order_xx_intermediate(self.shiba, R12, R23, R31)
        couplings[(3, 3)] = mea.third_order_xx_intermediate(self.shiba, R12, R23, R31)
        return couplings

    def chiral_interaction(self, R12: float, R23: float, R31: float):
        """
        Return the chiral interaction between three spins.
        """
        return mea.chiral_interaction(self.shiba, R12, R23, R31)
