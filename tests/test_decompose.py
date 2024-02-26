from ..module.decomposition import decompose
import numpy as np

import pytest

matrix = np.eye(2)

testmatrix = np.kron(matrix, matrix)


def test_decompose_indenity():
    assert decompose(testmatrix)[(0, 0)] == 1
