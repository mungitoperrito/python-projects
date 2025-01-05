# ch01
# https://testautomationu.applitools.com/pytest-tutorial/chapter1.html

# ch02
# https://testautomationu.applitools.com/pytest-tutorial/chapter2.html

# Original test case
def test_one_plus_one():
    assert 1 + 1 == 2

# ch02 updated test case
def test_one_plus_two():
    a = 1
    b = 2
    c = 0  # Failing test
    assert a + b == c
