import numpy as np
from src.coupling import Coupling


# Example of how to use the the code
#
def params():
    # The lattice unit vectors in the Cartesian coordinate
    vec1 = np.array([1, 0])
    vec2 = np.array([0, 1])
    # The lattice spacing in meter
    R = 1
    # The dimensionless exchange coupling
    alpha = 0.9
    # The small perturbative parameter for the spin flip term
    beta = 1
    # Fermi wavelength in meter
    lambdaF = 1
    # Superconductor coherence length in meter
    xi = 1
    # Magnetic field in Tesla
    B = 1
    return [vec1, vec2, R, alpha, beta, lambdaF, xi, B]


if __name__ == "__main__":
    # Inititate the coupling class
    shib = Coupling(*params())

    # Compute the effecitve coupling for the second order perturbation
    # between impurities at coordinate (1,0) and (0,0)
    second = shib.secondOrder([0, 1], [0, 0])

    # All of the paramters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # You can find the actualy distance between two points
    # at coord1 and coord2
    print(f"Distance between two point : {shib.lat.distance([1,0], [0,0])}\n")

    # Compute the effecitve coupling for the third order perturbation
    # between impurities at coordinate (0,1), (0, 0), and (1,0)
    third = shib.thirdOrder([0, 1], [0, 0], [1, 0])

    # the result is store in the dictionary where the key is the tuple of pauli string
    # E.g. (0,0,1) = IIX, (1,2,3) = XYZ
    print("Second order perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, value)
    print("=============================================\n")
    print("Third order perturbation")
    for key, value in third.items():
        if value != 0.0:
            print(key, value)
