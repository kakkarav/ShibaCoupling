import numpy as np
import pytest


class Lattice:
    def __init__(self, B, R) -> None:
        self.lattice = None
        self.site = True
        self.spacing = x


def test():
    for i in range(3):
        print(i)
    return 4


def test5():
    for j in range(5):
        print(j)
    return 6


# I want to write a code that generate a fibonacci sequence
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# i want to create a Test class that test the fib function
class TestLattice:
    def test_fib(self):
        assert fib(10) == 55

    def test_fib2(self):
        assert fib(20) == 6765

    def test_fib3(self):
        assert fib(30) == 832040


# A function that create a Lattice class that who about the properties of 2D cubic lattice.
#  This has many attribute of a lattice such as the lattic spacing and the nuber of size
class Lattice:
    def __init__(self, B, R) -> None:
        self.lattice = None
        self.site = True
        self.spacing = x

    # a method that compute the distance between any arbitrary two sites on the lattice
    # I want to annotate the type of the return value of the method
    def distance(self, x, y) -> float:
        return np.sqrt(np.sum((x - y) ** 2))
