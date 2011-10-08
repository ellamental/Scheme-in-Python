"""
scheme_types.py
(c)2011 Nick Zarczynski
"""

class Symbol(str):
  """A symbol is an immutable string, but must be its own type."""
  pass

class The_Empty_List():
  """The empty list is used as a list terminator and should be a singleton"""
  def __repr__(self):
    return "()"

the_empty_list = The_Empty_List()
