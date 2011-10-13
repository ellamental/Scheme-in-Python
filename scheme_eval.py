"""
scheme_eval.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_eval import scheme_eval
"""

from scheme_types import Symbol, Pair

frame = {'test':"Value retrieved successfully"}

def lookup_symbol_value(symbol):
  try:
    return frame[symbol]
  except KeyError:
    return "Error: Unbound variable"

def self_evaluating(expr):
  t = type(expr)
  return t is int or t is float or t is str or t is bool

def scheme_eval(expr):
  if self_evaluating(expr):
    return expr
  elif type(expr) is Symbol:
    return lookup_symbol_value(expr)
  elif type(expr) is Pair:
    if expr.car == "define":
      frame[expr.cdr.car] = scheme_eval(expr.cdr.cdr.car)
      return "set symbol -> value"
    else:
      return "scheme_eval: not implemented"
  else:
    return "scheme_eval: not implemented"
