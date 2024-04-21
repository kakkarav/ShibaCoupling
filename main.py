# Example of how to use the the module
import numpy as np
from src.coupling import Coupling
from src.classes.params import Params


params = Params(
    # The unit vectors in the Cartesian coordinate
    vec1=np.array([1, 0]),
    vec2=np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)]),
    # The lattice spacing in meter
    R=np.sqrt(2) / 2 / np.pi,
    # The dimensionless exchange coupling
    alpha=0.98,
    # The small perturbative parameter for the spin flip term
    beta=1,
    # Fermi wavelength in meter
    lambda_F=0.001,
    # Superconductor coherence length in meter
    xi=1000,
    # Magnetic field in Tesla
    B=1,
)


if __name__ == "__main__":
    # Inititate the coupling class
    shib = Coupling(params)

    R = 10.0
    # Compute the effecitve coupling for the second order perturbation between impurities at coordinate (1,0) and (0,0)
    second = shib.second_order_approx(R)

    # All of the paramters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # Compute the effecitve coupling for the third order perturbation between impurities at coordinate (0,1), (0, 1), and (1,1)
    R12 = 10.0
    R23 = 10.0
    R31 = 10.0
    third = shib.third_order_approx(R12, R23, R31)

    scalar_chirality = shib.chiral_interaction(R12, R23, R31)
    # the result is store in the dictionary where the key is the tuple of pauli string e.g. (0,0,1) = IIX, (1,2,3) = XYZ

    # Print out the result for J^(2)
    print("=============================================\n")
    print("Second-order two-body perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, value)

    # Print out the result for J^(3)
    print("=============================================\n")
    print("Third-order two-body perturbation")
    for key, value in third.items():
        if np.abs(value) != 0:
            print(key, value)

    # Print out the result for J^(3)
    print("=============================================\n")
    print("Third-order chiral perturbation")
    print(scalar_chirality)
