# Example of how to use the module
import numpy as np
from src.coupling import Coupling
from src.classes.params import Params

# We use the parameters of SrTiO3
params = Params(
    # The unit vectors in the Cartesian coordinate
    vec1=np.array([1, 0]),
    vec2=np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)]),
    # The lattice spacing in nanometer
    R=np.sqrt(2) / 2 / np.pi,
    # The dimensionless exchange coupling (<1)
    alpha=0.98,
    # The small perturbative parameter for the spin flip term (<<1)
    beta=0.1,
    # Fermi wavelength in nanometer
    lambda_F=10.0,
    # Superconductor coherence length in nanometer
    xi=50.0,
    # Magnetic field in Tesla
    B=0.1,
)


if __name__ == "__main__":
    # Initiate the coupling class
    # We will ignore the lattice function here
    shib = Coupling(params)

    R = 3.0
    # Compute the effective coupling for the second order perturbation between impurities separated by distance R
    # J^{(2)}_{\alpha \beta}
    second = shib.second_order_approx(R)

    # All of the parameters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # Consider three spins with separation R12, R23, and R31
    R12 = 3.0
    R23 = 3.0
    R31 = 3.0

    # Compute the third-body two-body interactions
    # We assume three impurities here.
    # For a lattice, we need to sum over the third spin to get the final third order coupling
    # J^{(3)}_{\alpha \beta \gamma}
    third = shib.third_order_approx(R12, R23, R31)

    # Compute the third-body scalar chirality interaction
    # J^{\Delta}_{\alpha \beta \gamma}
    scalar_chirality = shib.chiral_interaction(R12, R23, R31)

    # the result is store in the dictionary where the key is the tuple of Pauli string e.g. (0,0,1) = IIX, (1,2,3) = XYZ

    # Print out the result for J^{(2)}_{\alpha \beta}
    print("=============================================\n")
    print("Second-order two-body perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, ":", value)

    # Print out the result for J^{(3)}_{\alpha \beta \gamma}
    print("=============================================\n")
    print("Third-order two-body perturbation")
    for key, value in third.items():
        if np.abs(value) != 0:
            print(key, ":", value)

    # Print out the result for J^(\Delta)_{\alpha \beta \gamma}
    print("=============================================\n")
    print("Third-order chiral perturbation")
    print("Chiral :", scalar_chirality)
