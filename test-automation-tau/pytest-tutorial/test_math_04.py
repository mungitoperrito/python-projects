# ch04
# https://testautomationu.applitools.com/pytest-tutorial/chapter4.html

import pytest

# ch04 equivalence classes, parameterization
products = [
    (2, 3, 6),       # positive integers
    (1, 99, 99),     # identity
    (0, 99, 0),      # zero
    (3, -4, -12),    # positive by negative
    (-5, -5, 25),    # negativ by negative
    (2.5, 3.0, 7.5)  # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_mutiplication(a, b, product):
    assert a * b == product

