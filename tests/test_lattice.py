import numpy as np
import pytest

import os
import sys

from src.coupling import Coupling


@pytest.fixture
def param():
    vec1 = np.array([1, 0])
    vec2 = np.array([0, 1])
    N = 10
    R = 1
    alpha = 1
    beta = 1
    lambdaF = 1
    xi = 1
    B = 1
    return [vec1, vec2, N, R, alpha, beta, lambdaF, xi, B]


@pytest.fixture
def Shib(param):
    return Coupling(*param)


def test_location(Shib):
    assert Shib.shiba.xi == 1


def test_distanc():
    pass


def test_area():
    pass
