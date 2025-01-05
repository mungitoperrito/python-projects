# ch03
# https://testautomationu.applitools.com/pytest-tutorial/chapter3.html

import pytest

# ch01 basic test case
def test_one_plus_one():
    assert 1 + 1 == 2

# ch02 failure test case
def test_one_plus_two():
    a = 1
    b = 2
    # c = 0  # Failing test
    c = 3  # Fixed test
    assert a + b == c

# ch03 assertion error handling
def test_divide_by_zero():
    good_int = 1
    zero = 0

   with pytest.raises(ZeroDivisionError) as e:
       num = good_int / zero

   assert 'division by zero'in str(e)