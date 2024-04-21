# ShibaCoupling

The python package for generating effective couplings between spin 1/2 magnetic impurities inside a superconductor in the presence of a transverse magnetic field.

The package is only designed to generate parameters for model building and to be used in conjunction with other numerical simulation technique such as DMRG, QMC, etc.

# Installation

The dependencies can be installed by running the following command from the root directory of the package:

```python
pip install -r requirements.txt
```

# Usage

The magnetic impurities form a two-dimensional lattice spanned by unit vectors `vec1` and `vec2`.

All couplings are given in the Pauli string basis, i.e.

```math
H_{\text{eff}} = \sum_{i,j} \sum_{\alpha, \beta} J_{\alpha, \beta} \sigma_{\alpha}^i \sigma_{\beta}^j
+ \sum_{i,j,k} \sum_{\alpha, \beta, \gamma} J_{\alpha \beta \gamma}^{\Delta} \sigma_{\alpha}^i \sigma_{\beta}^j \sigma_{\gamma}^k
```

where $\alpha, \beta = x, y, z$ and $\sigma_{\alpha}$ are the Pauli matrices and $\alpha \beta \gamma$ are the impurity indices. $J_{\alpha \beta}$ and $J_{\alpha \beta \gamma}^{\Delta}$ are the second and the third effective coupling between the impurities respectively.

Specifically, the two-body term $J_{\alpha \beta} = J^{(2)}_{\alpha \beta} + J^{(3)}_{\alpha \beta}$ contains the contributions from the second and the third perturbation.
To obtain the third order contribution $J^{(3)}_{\alpha \beta} = \sum_{ \gamma \neq \alpha \beta} J^{(3)}_{\alpha \beta \gamma}$, we need sum over the third spectator spin.

# Parameters

- `vec1` (numpy.ndarray): The first lattice unit vector in Cartesian coordinate
- `vec2` (numpy.ndarray): The second lattice unit vector in Cartesian coordinate
- `R` (float): The lattice spacing in nanometer
- `alpha` (float): The dimensionless exchange coupling between the impurity and the electron spin. (<1)
- `beta` (float): The dimension anisotropy parameter (<<1)
- `lambda_F` (float): The Fermi wavelength in nanometer
- `xi` (float): The superconducting coherence length in nanometer
- `B` (float): The magnetic field strength in Tesla

# Example

An example for generating 2-body and 3-body interaction for a square lattice is given in main.py:

```python
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

    # the spin separation in the unit of Fermi wavelength
    R = 10.0

    # Compute the effective coupling for the second order perturbation between impurities separated by distance R
    # J^{(2)}_{\alpha \beta}
    second = shib.second_order_approx(R)

    # All of the parameters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # Consider three spins with separation R12, R23, and R31
    R12 = 10.0
    R23 = 10.0
    R31 = 10.0

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

```

To test this script, run:

```python
python main.py
```
