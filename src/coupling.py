from src.classes import params, lattice
from src import matrix_element as me
from src import matrix_element_approx as mea
import numpy as np


class Coupling:
    def __init__(self, parameters: params.Params):
        self.lat = lattice.Lattice(parameters)
        self.shiba = params.Shiba(parameters)

    def secondOrder(self, coord1: np.ndarray, coord2: np.ndarray):
        """
        Return a dictionary contain all coupling.
        We will get 2-body interaction but will will also include the third spin for consistency
        """
        return me.secondOrder(self.lat, self.shiba, coord1, coord2)

    def thirdOrder(self, coord1: np.ndarray, coord2: np.ndarray, coord3: np.ndarray):
        """
        Return a dictioanry contain all coupling where the order of the operator index are conserved.
        correspond to the orfer of the coordoinate
        """
        return me.thirdOrder(self.lat, self.shiba, coord1, coord2, coord3)

    def secondOrderApprox(self, coord1: np.ndarray, coord2: np.ndarray):
        """
        Return a dictionary contain all coupling.
        We will get 2-body interaction but will will also include the third spin for consistency
        """
        return mea.secondOrder(self.lat, self.shiba, coord1, coord2)

    def thirdOrderApprox(
        self, coord1: np.ndarray, coord2: np.ndarray, coord3: np.ndarray
    ):
        """
        Return a dictioanry contain all coupling where the order of the operator index are conserved.
        correspond to the orfer of the coordoinate
        """
        return mea.thirdOrder(self.lat, self.shiba, coord1, coord2, coord3)
