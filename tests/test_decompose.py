import numpy as np


from src import decomposition as decom

pauli = {}
pauli[0] = np.eye(2)
pauli[1] = np.array([[0.0, 1.0], [1.0, 0.0]])
pauli[2] = np.array([[0.0, -1j], [1j, 0.0]])
pauli[3] = np.array([[1.0, 0.0], [0, -1.0]])


# Test 2-body decompostion
def test_decompose_indenity1():
    for i in range(3):
        for j in range(3):
            testmatrix = np.kron(pauli[i], pauli[j])
            result = decom.decompose(testmatrix)
            for k1, k2 in result.keys():
                if k1 == i and k2 == j:
                    assert result[(k1, k2)] == 1
                else:
                    assert result[(k1, k2)] == 0


# Test 3-body decompostion
def test_decompose_indenity2():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                testmatrix = np.kron(np.kron(pauli[i], pauli[j]), pauli[k])
                result = decom.decompose(testmatrix)
                for k1, k2, k3 in result.keys():
                    if k1 == i and k2 == j and k3 == k:
                        assert result[(k1, k2, k3)] == 1
                    else:
                        assert result[(k1, k2, k3)] == 0


# Test 3-body decompostion
def test_decompose_indenity3():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                testmatrix = np.kron(np.kron(pauli[i], pauli[j]), pauli[k])
                testmatrix = testmatrix + np.kron(np.kron(pauli[1], pauli[2]), pauli[3])
                result = decom.decompose(testmatrix)
                for k1, k2, k3 in result.keys():
                    if k1 == i and k2 == j and k3 == k:
                        assert result[(k1, k2, k3)] == 1
                    elif k1 == 1 and k2 == 2 and k3 == 3:
                        assert result[(k1, k2, k3)] == 1
                    else:
                        assert result[(k1, k2, k3)] == 0
