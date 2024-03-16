# Example of how to use the the module
import numpy as np
from src.coupling import Coupling
from src import matrixElement as me
from src.classes.params import Params


params = Params(
    vec1=np.array([1, 0]),
    vec2=np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)]),
    R=np.sqrt(2) / 2 / np.pi,
    alpha=0.98,
    beta=1,
    lambda_F=0.001,
    xi=1000,
    B=100,
)


if __name__ == "__main__":
    # Inititate the coupling class
    shib = Coupling(params)

    # Compute the effecitve coupling for the second order perturbation
    # between impurities at coordinate (1,0) and (0,0)
    second = shib.secondOrder([0, 1], [0, 2])

    # All of the paramters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # You can find the actualy distance between two points
    # at coord1 and coord2
    coord1 = np.array([1, 0])
    coord2 = np.array([0, 1])
    print(f"Distance between two point : {shib.lat.distance(coord2, coord2)}\n")

    # Compute the effecitve coupling for the third order perturbation
    # between impurities at coordinate (0,1), (0, 0), and (1,0)
    third = shib.thirdOrder([0, 4], [0, 5], [0, 6])

    # the result is store in the dictionary where the key is the tuple of pauli string
    # E.g. (0,0,1) = IIX, (1,2,3) = XYZ

    # Print out the result
    print("Second order perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, value)

    print("=============================================\n")
    print("Third order perturbation")
    for key, value in third.items():
        if np.abs(value) != 0:
            print(key, value)

    print("=============================================\n")
