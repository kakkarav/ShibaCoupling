import numpy as np
from numpy import cos, sin, pi, exp, sqrt
from src.classes.params import Shiba


def normalized_spatial_part(shib: Shiba, R: float):
    """
    The normalization and the spatial part of the YSR wavefunction
    R is the in the unit of Fermi wavelength
    """
    alpha = shib.alpha
    xi = shib.xi
    normalization = 4 * alpha**2 / (1 + alpha**2) ** (3 / 2)
    decay = exp(-R / xi) / (2 * np.pi * R)
    return normalization * decay


def second_order_zz(shib: Shiba, R: float):
    """
    The zz two-body interaction between two spins
    """
    normalization = normalized_spatial_part(shib, R)
    excitation_energy = shib.energy * 2
    jzz = (
        -(normalization**2)
        * (1 + 8 * (shib.beta**2))
        / 2.0
        * (cos(2 * pi * R) ** 2)
        * (sin(shib.delta) ** 2)
        / excitation_energy
    )
    return jzz


def second_order_xx(shib: Shiba, R: float):
    """
    The xx and yy two-body interaction between two spins
    """
    normalization = normalized_spatial_part(shib, R)
    excitation_energy = shib.energy * 2
    jxx = (
        -(normalization**2)
        * 4
        * (shib.beta**2)
        * (cos(2 * pi * R) ** 2)
        * (sin(shib.delta) ** 2)
        / excitation_energy
    )
    return jxx


def third_order_zz_intermediate(shib: Shiba, R12: float, R23: float, R31: float):
    """
    This zz third-order two-body spin interaction between spin at site 1 and site 2
    due to the presence of spin at site 3.
    To find the total effective interaction, we must sum the interaction over the third spin.
    """
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    excitation_energy = shib.energy * 2
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
        * (sin(shib.delta) ** 2)
        * (sin(shib.delta) ** 2)
        * cos(shib.delta)
        / (excitation_energy**2)
    )
    return jzz


def third_order_xx_intermediate(shib: Shiba, R12: float, R23: float, R31: float):
    """
    This xx and yy third-order two-body spin interaction between spin at site 1 and site 2
    due to the presence of spin at site 3.
    To find the total effective interaction, we must sum the interaction over the third spin.
    """
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    excitation_energy = shib.energy * 2
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
        * (sin(shib.delta) ** 2)
        * (sin(shib.delta) ** 2)
        * cos(shib.delta)
        / (excitation_energy**2)
    )
    return jxx


def chiral_interaction(shib: Shiba, R12: float, R23: float, R31: float):
    s = (R12 + R23 + R31) / 2.0
    area = sqrt(s * (s - R12) * (s - R23) * (s - R31))
    flux = area * shib.B
    n1 = normalized_spatial_part(shib, R12)
    n2 = normalized_spatial_part(shib, R23)
    n3 = normalized_spatial_part(shib, R31)
    excitation_energy = shib.energy * 2
    return (
        -(n1 * n2 * n3)
        * 2
        * (shib.beta**2)
        * sin(2 * pi * flux / shib.quantum_flux)
        * sin(shib.delta) ** 3
        * cos(2 * np.pi * R12)
        * cos(2 * np.pi * R23)
        * cos(2 * np.pi * R31)
        / (excitation_energy**2)
    )
