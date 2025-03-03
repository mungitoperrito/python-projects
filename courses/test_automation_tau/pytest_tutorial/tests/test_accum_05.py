# ch05
# https://testautomationu.applitools.com/pytest-tutorial/chapter5.html

# # DEBUG
# import sys
# for p in sys.path:
#   print(p)

import pytest
from stuff.accum import Accumulator  # Fails with c> pytest
                                     #  module path not correct
                                     # Works with c> python -m pytest


def test_accumulator_init():
  a = Accumulator()
  assert a.count == 0

def test_accumulator_add_one():
  a = Accumulator()
  a.add()
  assert a.count == 1

def test_accumulator_add_three():
  a = Accumulator()
  a.add(3)
  assert a.count == 3

def test_accumulator_add_twice():
  a = Accumulator()
  a.add()
  a.add()
  assert a.count == 2

def test_accumulator_cannot_set_count_directly():
  a = Accumulator()
  with pytest.raises(AttributeError,
    match=r"property 'count' of 'Accumulator' object has no setter") as e:

    a.count = 10