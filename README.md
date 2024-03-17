# ShibaCoupling

The python package for generating effective couplings between spin 1/2 magnetic impurity inside a superconductor in the presence of a transverse magnetic field.

The package is only designed to generate parameters for model building and to be used in conjunction with other numerical simulation technique such as DMRG, QMC, etc.

All couplings are given in the Pauli string basis.


# Installation 

The dependencies can be installed by running the following command in the terminal
```python
pip install -r requirements.txt
```

# Example


An example for generating 2-body and 3-body interaction for a square lattice is given in main.py: 

```python
import numpy as np
from src.coupling import Coupling
from src import matrixElement as me
from src.classes.params import Params


params = Params(
  vec1=np.array([1, 0]),
  vec2=np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)]),
  R=np.sqrt(2) / 2 / np.pi,
  alpha=0.98,
  beta=1,
  lambda_F=0.001,
  xi=1000,
  B=100,
)


# Initiate the coupling class
shib = Coupling(params)

# Compute the effective coupling for the second order perturbation
# between impurities at coordinate (1,0) and (0,0)
second = shib.secondOrder([0, 1], [0, 2])

# All of the parameters are stored in
print("Here are the model paramters")
print(shib.shiba)

# You can find the actual distance between two points
# at coord1 and coord2
coord1 = np.array([1, 0])
coord2 = np.array([0, 1])
print(f"Distance between two point : {shib.lat.distance(coord2, coord2)}\n")

# Compute the effective coupling for the third order perturbation
# between impurities at coordinate (0,1), (0, 0), and (1,0)
third = shib.thirdOrder([0, 4], [0, 5], [0, 6])

# the result is store in the dictionary where the key is the tuple of Pauli string
# E.g. (0,0,1) = IIX, (1,2,3) = XYZ

# Print out the couplings 
print("Second order perturbation")
for key, value in second.items():
  if value != 0.0:
    print(key, value)

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

