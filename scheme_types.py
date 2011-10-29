"""
scheme_types.py
(c)2011 Nick Zarczynski
License: BSD
"""

class Symbol(str):
  """A symbol is an immutable string, but must be its own type."""
  pass

class The_Empty_List():
  """The empty list is used as a list terminator and should be a singleton"""
  def __repr__(self):
    return "()"

the_empty_list = The_Empty_List()

class Pair(object):
  """A pair is a classic Lisp cons cell used to implement lists"""
  def __init__(self, car, cdr):
    self.car = car
    self.cdr = cdr
  def __iter__(self):
    x = self
    while not isinstance(x, The_Empty_List):
      yield x.car
      x = x.cdr
  def __repr__(self):
    return "(" + ' '.join([str(i) for i in list(self)]) + ")"

class Primitive(object):
  def __init__(self, fn):
    self.fn = fn

class Procedure(object):
  def __init__(self, parameters, body, environment):
    self.parameters = parameters
    self.body = body
    self.environment = environment
