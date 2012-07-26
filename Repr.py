from implements import *

class Repr(Interface):
  __name__ = "Repr"
  __interface__ = ["__repr__"]

@implementing(Repr)
class MyThing(object):
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "MyThing: " + self.name
