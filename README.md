# ShibaCoupling

The python package for generating effective couplings between spin 1/2 magnetic impurities inside a superconductor in the presence of a transverse magnetic field.

The package is only designed to generate parameters for model building and to be used in conjunction with other numerical simulation technique such as DMRG, QMC, etc.


# Installation 

The dependencies can be installed by running the following command from the root directory of the package:

```python
pip install -r requirements.txt
```

# Usage

The magnetic impurities form a two dimensional lattice spanned by unit vectors `vec1` and `vec2`.

All couplings are given in the Pauli string basis, i.e.

```math
H_{\text{eff}} = \sum_{i,j} \sum_{\alpha, \beta} J_{\alpha, \beta}^{(2)} \sigma_{\alpha}^i \sigma_{\beta}^j
+ \sum_{i,j,k} \sum_{\alpha, \beta, \gamma} J_{\alpha, \beta, \gamma}^{(3)} \sigma_{\alpha}^i \sigma_{\beta}^j \sigma_{\gamma}^k
```

where $\alpha, \beta = x, y, z$ and $\sigma_{\alpha}$ are the Pauli matricesm and $i,j,k$ are the impurity indices.

$J_{\alpha, \beta}^{(2)}$ and $J_{\alpha, \beta, \gamma}^{(3)}$ are the second and the third effective coupling between the impurities respectively.

# Parameters

- `vec1` (numpy.ndarray): The first lattice unit vector in Cartesian coordinate
- `vec2` (numpy.ndarray): The second lattice unit vector in Cartesian coordinate
- `R` (float): The lattice spacing in meter
- `alpha` (float): The dimensionless exchange coupling between the impurity and the electron spin
- `beta` (float): The dimension anisotropy parameter 
- `lambda_F` (float): The Fermi wavelength in meter 
- `xi` (float): The superconducting coherence length
- `B` (float): The magnetic field strength

# Example


An example for generating 2-body and 3-body interaction for a square lattice is given in main.py: 

```python
# Example of how to use the the module
import numpy as np
from src.coupling import Coupling
from src.classes.params import Params


params = Params(
    # The unit vectors in the Cartesian coordinate
    vec1=np.array([1, 0]),
    vec2=np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)]),
    # The lattice spacing in meter
    R=np.sqrt(2) / 2 / np.pi,
    # The dimensionless exchange coupling
    alpha=0.98,
    # The small perturbative parameter for the spin flip term
    beta=1,
    # Fermi wavelength in meter
    lambda_F=0.001,
    # Superconductor coherence length in meter
    xi=1000,
    # Magnetic field in Tesla
    B=100,
)


if __name__ == "__main__":
    # Inititate the coupling class
    shib = Coupling(params)

    # Create coordinates for three impurities
    coord1 = np.array([1, 0])
    coord2 = np.array([0, 1])
    coord3 = np.array([1, 1])

    # Compute the effecitve coupling for the second order perturbation between impurities at coordinate (1,0) and (0,0)
    second = shib.secondOrder(coord1, coord2)

    # All of the paramters are stored in
    print("Here are the model paramters")
    print(shib.shiba)

    # You can find the actualy distance between two points at coord1 and coord2
    print(f"Distance between two point : {shib.lat.distance(coord2, coord2)}\n")

    # Compute the effecitve coupling for the third order perturbation between impurities at coordinate (0,1), (0, 1), and (1,1)
    third = shib.thirdOrder(coord1, coord2, coord3)

    # the result is store in the dictionary where the key is the tuple of pauli string e.g. (0,0,1) = IIX, (1,2,3) = XYZ

    # Print out the result for 2-body coupling J^(2)
    print("=============================================\n")
    print("Second order perturbation")
    for key, value in second.items():
        if value != 0.0:
            print(key, value)

    # Print out the result for 3-body coupling J^(3)
    print("=============================================\n")
    print("Third order perturbation")
    for key, value in third.items():
        if np.abs(value) != 0:
            print(key, value)
```

To test this script, run:

```python
python main.py
```

