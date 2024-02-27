import numpy as np
import pytest

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
    assert all((Shib.lat.location([1, 1]) - np.array([1, 1])) == 0)
    assert all((Shib.lat.location([-1, -1]) - np.array([-1, -1])) == 0)
    assert all((Shib.lat.location([1, 0]) - np.array([1, 0])) == 0)
    assert all((Shib.lat.location([0, 1]) - np.array([0, 1])) == 0)
    assert all(Shib.lat.location([0, 0]) == 0)


def test_distance(Shib):
    p1 = np.array([1, 0])
    p2 = np.array([0, 1])
    assert Shib.lat.distance(p1, p2) == np.sqrt(2)

    p1 = np.array([-1, 0])
    p2 = np.array([0, -1])
    assert Shib.lat.distance(p1, p2) == np.sqrt(2)

    p1 = np.array([0, 1])
    p2 = np.array([1, 0])
    assert Shib.lat.distance(p1, p2) == np.sqrt(2)

    p1 = np.array([1, 0])
    p2 = np.array([1, 0])
    assert Shib.lat.distance(p1, p2) == 0.0

    p1 = np.array([5, 0])
    p2 = np.array([0, 0])
    assert Shib.lat.distance(p1, p2) == 5.0

    p1 = np.array([0, 0])
    p2 = np.array([5, 0])
    assert Shib.lat.distance(p1, p2) == 5.0


def test_area(Shib):
    assert Shib.lat.area([0, 0], [1, 0], [0, 1]) == 0.5
    assert Shib.lat.area([0, 0], [0, 1], [1, 0]) == -0.5
    assert Shib.lat.area([1, 0], [0, 0], [0, 1]) == -0.5
    assert Shib.lat.area([0, 1], [0, 0], [1, 0]) == 0.5
    assert Shib.lat.area([1, 0], [0, 1], [0, 0]) == 0.5
    assert Shib.lat.area([0, 1], [1, 0], [0, 0]) == -0.5


def test_phase(Shib):
    B = 1
    # same point
    p1 = np.array([0, 0])
    p2 = np.array([0, 0])
    assert Shib.lat.phase(B, p1, p2) == 0.0

    # same point
    p1 = np.array([1, 0])
    p2 = np.array([1, 0])
    assert Shib.lat.phase(B, p1, p2) == 0.0

    # back and forth
    p1 = np.array([1, 0])
    p2 = np.array([0, 1])
    assert Shib.lat.phase(B, p1, p2) + Shib.lat.phase(B, p2, p1) == 0.0

    # back and forth
    p1 = np.array([1, 0])
    p2 = np.array([0, 1])
    assert Shib.lat.phase(B, p1, p2) + Shib.lat.phase(B, p2, p1) == 0.0

    # Go around a right triangle
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0, 1])
    # countercolckwise
    assert (
        Shib.lat.phase(B, p1, p2)
        + Shib.lat.phase(B, p2, p3)
        + Shib.lat.phase(B, p3, p1)
        == 0.5
    )
    # Clockwise
    assert (
        Shib.lat.phase(B, p1, p3)
        + Shib.lat.phase(B, p3, p2)
        + Shib.lat.phase(B, p2, p1)
        == -0.5
    )

    # Compare the flux with the area when B = 1
    p1 = np.array([2, 0])
    p2 = np.array([1, 3])
    p3 = np.array([0, 1])
    assert Shib.lat.phase(B, p1, p2) + Shib.lat.phase(B, p2, p3) + Shib.lat.phase(
        B, p3, p1
    ) == Shib.lat.area(p1, p2, p3)
