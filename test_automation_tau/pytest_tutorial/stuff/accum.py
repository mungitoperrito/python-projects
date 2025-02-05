# ch05
# https://testautomationu.applitools.com/pytest-tutorial/chapter5.html

class Accumulator:
  def __init__(self):
    self._count = 0

  @property
  def count(self):
    return self._count

  def add(self, more=1):
    self._count += more