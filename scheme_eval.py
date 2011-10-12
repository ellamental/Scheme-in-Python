"""
scheme_eval.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_eval import scheme_eval
"""

def self_evaluating(expr):
  t = type(expr)
  return t is int or t is float or t is str or t is bool

def scheme_eval(expr):
  if self_evaluating(expr):
    return expr
  else:
    return "scheme_eval: not implemented"
