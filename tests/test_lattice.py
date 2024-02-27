import numpy as np
import pytest

import os
import sys

from src.coupling import Coupling


@pytest.fixture
def shiba():
    return Coupling()


def test_location():
    shiba().shiba.xi
    pass


def test_distanc():
    pass


def test_area():
    pass
