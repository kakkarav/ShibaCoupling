import pytest
from src import matrixElement as me


def test_A():
    assert me.A(1, 1, 1) == 1
