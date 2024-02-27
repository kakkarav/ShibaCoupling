import numpy as np
from src.coupling import Coupling


def params():
    vec1 = np.array([1, 0])
    vec2 = np.array([0, 1])
    N = 10
    R = 1
    alpha = 1
    beta = 1
    lambdaF = 1
    xi = 1
    B = 0
    return [vec1, vec2, N, R, alpha, beta, lambdaF, xi, B]


if __name__ == "__main__":
    shib = Coupling(*params())
    # print(shib.secondOrder([0, 1], [0, 0]))
    # print(shib.thirdOrder([0, 1], [0, 0], [1, 0]))
    second = shib.secondOrder([0, 1], [0, 0])

    third = shib.thirdOrder([0, 1], [0, 0], [1, 0])
    print("Second order perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, value)
    print("Third order perturbation")
    for key, value in third.items():
        if value != 0.0:
            print(key, value)
