import numpy as np
from numpy import cos, sin, pi, exp
from src.classes.params import Shiba
from src.classes.lattice import Lattice


def normalized_spatial_part(shib: Shiba, R: float):
    alpha = shib.alpha
    xi = shib.xi
    normalization = 4 * alpha**2 / (1 + alpha**2) ** (3 / 2)
    decay = exp(-R / xi) / (2 * np.pi * R)
    return normalization * decay


def second_order_zz(shib: Shiba, R: float):
    normalization = normalized_spatial_part(shib, R)
    jzz = (
        -(normalization**2)
        * (1 + 8 * (shib.beta**2))
        / 2.0
        * cos(2 * pi * R)
        * (np.sin(shib.delta) ** 2)
    )
    return jzz


def second_order_xx(shib: Shiba, R: float):
    normalization = normalized_spatial_part(shib, R)
    jxx = (
        -(normalization**2)
        * 4
        * (shib.beta**2)
        * cos(2 * pi * R)
        * (np.sin(shib.delta) ** 2)
    )
    return jxx


def third_order_zz_intermediate(shib: Shiba, R12: float, R23: float, R31: float):
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    trig = (
        -sin(2 * pi * R12) * cos(2 * pi * R23) * cos(2 * pi * R31)
        + sin(2 * pi * R23) * cos(2 * pi * R31) * cos(2 * pi * R12)
        + sin(2 * pi * R31) * cos(2 * pi * R12) * cos(2 * pi * R23)
    )
    jzz = (
        -(n1 * n2 * n3)
        * (-1 + 4 * (shib.beta**2))
        / 2.0
        * trig
        * cos(shib.delta)
        * sin(shib.delta) ** 2
        * (np.sin(shib.delta) ** 2)
        * np.cos(shib.delta)
    )
    return jzz


def third_order_xx(shib: Shiba, R12: float, R23: float, R31: float):
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    trig = (
        -sin(2 * pi * R12) * cos(2 * pi * R23) * cos(2 * pi * R31)
        + sin(2 * pi * R23) * cos(2 * pi * R31) * cos(2 * pi * R12)
        + sin(2 * pi * R31) * cos(2 * pi * R12) * cos(2 * pi * R23)
    )
    jxx = (
        -(n1 * n2 * n3)
        * 2.0
        * (shib.beta**2)
        * trig
        * cos(shib.delta)
        * sin(shib.delta) ** 2
        * (np.sin(shib.delta) ** 2)
        * np.cos(shib.delta)
    )
    return jxx


def chiral_interaction(shib: Shiba, R12: float, R23: float, R31: float):
    s = (R12 + R23 + R31) / 2.0
    area = np.sqrt(s * (s - R12) * (s - R23) * (s - R31))
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    return (
        n1
        * n2
        * n3
        * cos(area * shib.B)
        * cos(shib.delta) ** 3
        * cos(2 * np.pi * R12)
        * cos(2 * np.pi * R23)
        * cos(2 * np.pi * R31)
    )
