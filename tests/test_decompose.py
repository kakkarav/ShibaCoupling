import numpy as np
import pytest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import decomposition as decom

matrix = np.eye(2)

testmatrix = np.kron(matrix, matrix)


def test_decompose_indenity():
    assert decom.decompose(testmatrix)[(0, 0)] == 1
